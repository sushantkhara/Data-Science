import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
import redis
import datetime

# Scraping data from a source


class Scraper:
    def __init__(self, keywords):
        self.markup = requests.get('https://news.ycombinator.com/').text
        self.keywords = keywords

# parsing html contents from the sources
    def parse(self):
        soup = BeautifulSoup(self.markup, 'html.parser')
        links = soup.findAll("a", {"class": "storylink"})
        self.saved_links = []
        for link in links:
            for keyword in self.keywords:
                if keyword in link.text:
                    self.saved_links.append(link)

# store links in redis db
    def store(self):
        r = redis.Redis(host='localhost', port=6379, db=0)
        for link in self.saved_links:
            r.set(link.text, str(link))

    def send_mail(self):
        r = redis.Redis(host='localhost', port=6379, db=0)
        links = [str(r.get(k)) for k in r.keys()]
        mail_content = """
                <h4> %s link/links you might find interesting today:</h4>
    
                %s
            """ % (len(links), '<br/><br/>'.join(links))

        # The mail addresses and password
        sender_address = 'digetbot@gmail.com'
        sender_pass = 'digestbot@2020'
        receiver_address = 'princesalomkhara@gmail.com'

        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = "News Links for today"  # The subject line

        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'html'))

        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(sender_address, sender_pass)  # login with mail_id and password
        print('Login Success!!')
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
        # flush redis to clear redis cache
        r.flushdb()


if __name__ == '__main__':
    s = Scraper(['code', 'Covid', 'Google', 'python', 'Django', 'Data Science', 'automating', 'automate', 'machine ',
                'learning', 'artificial intelligence', 'startup', 'freelance', 'data analysis', 'job', 'data scientist',
                 'deep', 'data', 'analysis', 'scrap', 'app', 'developer', 'project', 'Amazon', 'Apple', 'Microsoft',
                 'Facebook', 'Twitter', 'Instagram', 'hack', 'Netflix', 'database', 'analytics'])
    s.parse()
    s.store()
    if datetime.datetime.now().hour >= 20:
        s.send_mail()

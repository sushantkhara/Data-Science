import pyttsx3
import PyPDF2

audiobook = open('C:/Users/k96su/Downloads/Documents/BiblePromisesForMen.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(audiobook)
totalPages = pdfReader.numPages
engine = pyttsx3.init()    # create and initialize the object
for pages in range(22, totalPages):     # walk through pages to read the contents
    page = pdfReader.getPage(22)
    readContent = page.extractText()  # extract page texts
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(readContent)
    engine.runAndWait()
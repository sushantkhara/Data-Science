#If the Data is huge then to improve system performance we need Database in backend to acrryout all operations
import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word=input("Enter the word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()
print(type(results))
data = dict(results)
""" def thesaurus(word):
    word=word.lower()
    if word in results:
        return results[word]
    
    #if user entered "texas" this will check for "Texas" as well.
    elif word.title() in results:                        
        return results[word.title()]
    #in case user enters words like USA or NATO
    elif word.upper() in results: 
        return results[word.upper()]

    #if user enters the word which is not found in dictionary.extract similar words which are available,then return the word

    elif len(get_close_matches(word,results.keys())) > 0:
        choice = input("Did you mean %s instead? enter y for yes, or n for no: " % get_close_matches(word,results.keys())[0])     
        if choice == 'y':
            #it returns the first possible match
            return results[get_close_matches(word,results.keys())[0]]             
        elif choice == 'n':
            return 'Sorry! that word does not exist. Please check the word and type a correct one.'
        else:
            return "We didn't understand your response.Please"
    else:
        return "Entered word doesn't exist.Please check again and type correct word!" """

if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")
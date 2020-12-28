# If the Data is huge then to improve system performance we need Database in backend to carryout all operations
import mysql.connector
from difflib import get_close_matches
import sys

# open a database connection
con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)
# prepare a cursor object using cursor() method
cursor = con.cursor()


# function to search the user entry word
def thesaurus(word):
    word = word.lower()  # In case user types word in caps
    # execute the SQL query using execute() method.
    query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
    # fetch all of the rows from the query
    results = cursor.fetchall()
    if results:
        for result in results:
            print(result[0])
    # if user entered "texas" this will check for "Texas" as well.

    elif word.title() in results:
        for result in results:
            print(result[0])
    # in case user enters words like USA or NATO
    elif word.upper() in results:
        for result in results:
            print(result[0])
    else:
        print("Sorry! no word found!")
  
"""
# close the cursor object
cursor.close()

# close the connection
con.close() 

# exit the program
        sys.exit()"""
# take user input to look for the word
word = input("Enter the word: ")
thesaurus(word)

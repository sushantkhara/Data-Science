import json
from difflib import get_close_matches

#Loading JSON file
data=json.load(open('data.json'))

#Function to search the user entry word
def thesaurus(word):
    word=word.lower()
    if word in data:
        return data[word]    

    #if user entered "texas" this will check for "Texas" as well.
    elif word.title() in data:                        
        return data[word.title()]

    #in case user enters words like USA or NATO
    elif word.upper() in data: 
        return data[word.upper()]

    #if user enters the word which is not found in dictionary.extract similar words which are available,then return the word

    elif len(get_close_matches(word,data.keys())) > 0:
        choice = input("Did you mean %s instead? enter y for yes, or n for no: " % get_close_matches(word,data.keys())[0])     
        if choice == 'y':
            #it returns the first possible match
            return data[get_close_matches(word,data.keys())[0]]             
        elif choice == 'n':
            return 'Sorry! that word does not exist.'
        else:
            return "We didn't understand your entry."
    else:
        return "Entered word doesn't exist.Please check again!"

word = input("Hello there,Please Enter a word: ")

#To provide user-friendly result,assign value of the function call to a var and iterate it if the result is a list

output = thesaurus(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)




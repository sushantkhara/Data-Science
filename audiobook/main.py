import pyttsx3
import PyPDF2
import os

with open(filename, 'rb') as file:
    audiobook = PyPDF2.PdfFileReader(file)
audiobook = open('C:/Users/k96su/Downloads/Documents/BiblePromisesForMen.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(audiobook)
totalPages = pdfReader.numPages
engine = pyttsx3.init()    # create and initialize the object
for pages in range(0, totalPages):     # walk through pages to read the contents
    page = pdfReader.getPage(22)
    readContent = page.extractText()  # extract page texts
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(readContent)
    engine.runAndWait()
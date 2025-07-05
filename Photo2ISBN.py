import easyocr
import cv2
import requests
import json
import time
from itertools import combinations

#Test image, the actual input will be from the users camera
bookimage = 'TheShining.jpg'

#This loads the image for OpenCV
loaded_img = cv2.imread(bookimage)

#This loads the OCR model
reader = easyocr.Reader(['en'], gpu=False)

#This is what reads the text from the image
result = reader.readtext(loaded_img)

#The _'s is telling the return values to ignore that value, the values are bbox, text, confidence
texts = [text for _, text, _ in result]

#Empty list to store returned image in a format suitable for the API
queries = []

#Thus us what adds the queries to the lsit in the suitable format
#It works by extending the list with a bunch of combinations joined together by a space (joined together in 2s and 3s)
for size in [2,3]:
    queries.extend([' '.join(combo) for combo in combinations(texts, size)])

#Dictionary to store possible book data returned from the API
PossibleBooks = {}
#This set is used to make sure there are no copies of the same book data
Identifiers = set()

print("Showing Possible Books")

#For loop to request the data using all of the combinations of queries
for query in queries:
    r = requests.get(f'https://openlibrary.org/search.json?q={query}')
    #data is what holds the json data returned from the API
    data = r.json()

    #This gets the data found in the json data based on whether or not the number of books found is equal to or above one
    if data["numFound"] >= 1:
        title = data["docs"][0].get("title", "Unknown Title")
        author = data["docs"][0].get("author_name", ["Unknown Author"])[0]
        ISBN = data["docs"][0].get("ia", ["Unknown ISBN"])[0]

        #This checks for copies and skips it if it is
        if ISBN in Identifiers:
            continue

        print(f"\nBook: {title} by {author}")

        #This checks to see if the returned identifier was an ISBN or something different
        if ISBN[:5] != "isbn_":
            print(f"Internet Archive Identifier: {ISBN}")
        else:
            print(f"ISBN: {ISBN}")
        
        print(f"Link: {r.url}")

        #This adds the identifier so that the next loop knows what has already been requested
        Identifiers.add(ISBN)
        #This adds the returned data to the dictonary
        PossibleBooks[title] = (author, ISBN)
        #This is used to leave breathing room for the API requests
        time.sleep(0.5)

#This prints out the book titles received in a list format
print("\nPossible Book List:\n")
for title in PossibleBooks:
    print(f"Title: {title}")


#This section lets the user make sure out of the options that their books is there
print("\nIf your book is in the returned list type out its title")
book = input("Book: ")

if book in PossibleBooks:
    author, ISBN = PossibleBooks[book]
    print(f"\nThe book is {book} by {author}")
    print(f"ISBN: {ISBN[5:]}")
else:
    print("Book was not included in returned list")

#In the future, code will be added to add missing books or misfindings so that more accurate results are obtained
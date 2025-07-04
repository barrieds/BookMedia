import easyocr
import cv2
import requests
import json
from itertools import combinations

#Test image, the actual input will be from the users camera
bookimage = 'shiver.jpg'

#This loads the image for OpenCV
loaded_img = cv2.imread(bookimage)

#This loads the OCR model
reader = easyocr.Reader(['en'], gpu=False)

#This is what reads the text from the image
result = reader.readtext(loaded_img)

#The _'s is telling the return values to ignore that value, the values are bbox, text, confidence
texts = [text for _, text, _ in result]

queries = []

for size in [2,3]:
    queries.extend([' '.join(combo) for combo in combinations(texts, size)])

for query in queries:
    r = requests.get(f'https://openlibrary.org/search.json?q={query}')
    data = r.json()

    if data["numFound"] == 1:
        title = data["docs"][0].get("title", "Unknown Title")
        author = data["docs"][0].get("author_name", ["Unknown Author"])[0]
        ISBN = data["docs"][0].get("isbn_", "Unknown ISBN")
        print(f"Book: {title} by {author}")
        print(f"ISBN: {ISBN}")
        break
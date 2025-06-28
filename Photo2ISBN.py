import easyocr
import cv2
import requests

#Test image, the actual input will be from the users camera
bookimage = 'shiver.jpg'

#This loads the image for OpenCV
loaded_img = cv2.imread(bookimage)

#This loads the OCR model
reader = easyocr.Reader(['en'], gpu=False)

#This is what reads the text from the image
result = reader.readtext(loaded_img)

#This is the function that prints the text returned from the image
def print_text():
    #The _'s is telling the return values to ignore that value, the values are bbox, text, confidence
    for (_, text, _) in result:
        print(text)
        return text

print_text()

bookreq = print_text()

#requesting the query on the database website
r = requests.get(f'https://openlibrary.org/search.json?q={bookreq}')

#Printing the url and status code to check what data is returned from the query and if an error happened
print(f"URL: {r.url} Status Code: {r.status_code}\n")

#This loads the JSON from the returned data
jsonreturn = json.loads(r.content)

Title = (jsonreturn["docs"][0]["title"])
Author = (jsonreturn["docs"][0]["author_name"])

try:
    ISBN = (jsonreturn["docs"][0]["isbn_"])

except KeyError:
    ISBN = "ISBN could not be found"

#This part prints out the content found in the returned content
if Title == "" or Author == "":
    print("Title or Author was not found")

elif ISBN == "":
    print("ISBN number could not be found")

else:
    print(Title)
    print(Author[-2:2])
    print(ISBN)
import easyocr
import cv2
import requests

#Test image, the actual input will be from the users camera
bookimage = 'C:/Users/seamu/Documents/ComputerWork/kingofbirds.jpg'

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

print_text()
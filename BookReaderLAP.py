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
    spec1 = result[0][1]
    spec2 = result[1][1]
    spec3 = result[2][1]
    spec4 = result[3][1]

    print(spec1)
    print(spec2)
    print(spec3)
    print(spec4)

    #The _'s is telling the return values to ignore that value, the values are bbox, text, confidence
    for (_, text, _) in result:
        print(text)

print_text()
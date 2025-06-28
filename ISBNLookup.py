import requests
import json

#Temporary user inputs, this will soon be inputted using the text received from the image in the other program
bookreqtitle = input("Request Title: ")
bookreqauthor = input("Request Author: ")

#requesting the query on the database website
r = requests.get(f'https://openlibrary.org/search.json?title={bookreqtitle}&author={bookreqauthor}')

#Printing the url and status code to check what data is returned from the query and if an error happened
print(f"URL: {r.url} Status Code: {r.status_code}\n")

#This loads the JSON from the returned data
jsonreturn = json.loads(r.content)

Title = (jsonreturn["docs"][0]["title"])
Author = (jsonreturn["docs"][0]["author_name"])

try:
    ISBN = (jsonreturn["docs"][0]["ia"][0])

except KeyError:
    ISBN = "ISBN could not be found"

#This block of code looks for the text in the returned content by finding the start and end values of the searched strings.
#This block of code now is not in use due to finding about pythons JSON handling (Took too much time to fully delete this part out)
#Title = r.text[r.text.find(bookreqtitle):r.text.find(bookreqtitle)+len(bookreqtitle)]
#Author = r.text[r.text.find(bookreqauthor[0:-1]):r.text.find(bookreqauthor[0:-1])+len(bookreqauthor[0:-1])]
#ISBN = r.text[r.text.find("isbn_"):r.text.find("isbn_") + 18]

#This part prints out the content found in the returned content

TitleSTR = str(Title)
AuthorSTR = str(Author)
ISBNSTR = str(ISBN)

if TitleSTR == "" or AuthorSTR == "":
    print("Title or Author was not found")

elif ISBNSTR == "":
    print("ISBN number could not be found")

else:
    print(f'Title: {TitleSTR}')
    print(f'Author: {AuthorSTR[2:][:-2]}')
    print(f'ISBN: {ISBNSTR[5:]}')

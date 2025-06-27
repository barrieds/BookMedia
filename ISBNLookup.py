import requests

#Temporary user inputs, this will soon be inputted using the text received from the image in the other program
bookreqtitle = input("Request Title: ")
bookreqauthor = input("Request Author: ")

#requesting the query on the database website
r = requests.get(f'https://openlibrary.org/search.json?title={bookreqtitle}&author={bookreqauthor}')

#Printing the url and status code to check what data is returned from the query and if an error happened
print(f"URL: {r.url} Status Code: {r.status_code}\n")

#This block of code looks for the text in the returned content by finding the start and end values of the searched strings.
Title = r.text[r.text.find(bookreqtitle):r.text.find(bookreqtitle)+len(bookreqtitle)]
Author = r.text[r.text.find(bookreqauthor[0:-1]):r.text.find(bookreqauthor[0:-1])+len(bookreqauthor[0:-1])]
ISBN = r.text[r.text.find("isbn_"):r.text.find("isbn_") + 18]

#This part prints out the content found in the returned content
if Title == "" or Author == "":
    print("Title or Author was not found")

elif ISBN == "":
    print("ISBN number could not be found")

else:
    print(Title)
    print(Author + bookreqauthor[-1:])
    print(f"ISBN: {ISBN[5:]}")
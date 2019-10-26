


# this web scrapping program helps to u search anything on the google bu just typing the name of that things and our our program takes u to the google related to that objects

import requests
from bs4 import BeautifulSoup
import webbrowser

user_input=input("enter the data which u want to search : ")
response=requests.get("https://www.google.com/search?source=hp&ei=aeEZXcmWK977z7sP852rsA8&q="+ user_input)

# print(response.text) we use bs4 instead of directly printing

soup=BeautifulSoup(response.text,"html.parser")
# print(soup.prettify())

results=soup.select(".jfp3ef a")    # return a list of <a> tag present in jfp3ef class
# print(results)
webbrowser.open("https://www.google.com/search?source=hp&ei=aeEZXcmWK977z7sP852rsA8&q="+user_input)
for link in results[:5]:
    final_links=link.get("href")
    webbrowser.open("https://www.google.com"+final_links)

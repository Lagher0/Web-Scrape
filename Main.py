from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://docs.python.org/3/"

uClient = uReq(my_url) # Downloads the webpage
page_html = uClient.read() #Gets the HTML code from the page
uClient.close() #Closes the file object

page_soup = soup(page_html, "html.parser") # Converts it into soup/ puts in in BeautifulSoup allowing us to start parsing through the HTML code

print(page_soup.h1)
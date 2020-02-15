from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.milkround.com/jobs/software-engineer?s=header"

uClient = uReq(my_url) # Downloads the webpage
page_html = uClient.read() #Gets the HTML code from the page
uClient.close() #Closes the file object

page_soup = soup(page_html, "html.parser") # Converts it into soup/ puts in in BeautifulSoup allowing us to start parsing through the HTML code



job_url = [] 

for job_titles in page_soup.findAll("div",{"class": "job-title"}): #  finds all div section with the class of job titles
    temp_a_link = job_titles.find("a", href = True) # Gets all <a> link tags that contain the links
    job_url.append(temp_a_link.get('href')) #Stores the links in the array
    


print(job_url)
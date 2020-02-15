from bs4 import BeautifulSoup as soup
import urllib.request as uReq
from lxml import etree


htmlparser = etree.HTMLParser()

def Prepare_Page(url):
    
    uClient = uReq.urlopen(my_url) # Downloads the webpage
    page_html = uClient.read() #Gets the HTML code from the page
    uClient.close() #Closes the file object

    page_soup = soup(page_html, "html.parser") # Converts it into soup/ puts in in BeautifulSoup allowing us to start parsing through the HTML code

    return page_soup

my_url = "https://www.jobsite.co.uk/jobs/software-developer"
page_soup = Prepare_Page(my_url)


job_url = [] 

for job_titles in page_soup.findAll("div",{"class": "job-title"}): #  finds all div section with the class of job titles
    temp_a_link = job_titles.find("a", href = True) # Gets all <a> link tags that contain the links
    job_url.append(temp_a_link.get('href')) #Stores the links in the array


url = 'https://www.totaljobs.com/job/software-developer/oscar-associates-uk-limited-job89574381?src=search&page=1&position=1&WT.mc_id=A_PT_CrossBrand_Jobsite&searchCriteria=Software+Developer&searchLocation=&source=jobsite'
print("I got here")

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
request = uReq.Request(url,headers={'User-Agent': user_agent})
response = uReq.urlopen(request)
html = response.read()
page_soup = soup(html, "html.parser")


def jobsite_Job_Info(page_soup):
    job_info = []
    job_title = page_soup.select('h1.brand-font')[0].text.strip()
    print(job_title)
    job_location = page_soup.find("li", {"class": "location icon"}).text.strip()
    print(job_location)
    job_salary = page_soup.find("li",{"class": "salary icon"}).text.strip()
    print(job_salary)
    job_company = page_soup.find("li",{"class": "company icon"}).text.strip()
    print(job_company)
    job_type = page_soup.find("li",{"class": "job-type icon"}).text.strip()
    print(job_type)
    date_posted = page_soup.find("li",{"class": "date-posted icon"}).text.strip()

    job_info.extend((job_title, job_salary, job_company, job_type, date_posted))
    return job_info
print(jobsite_Job_Info(page_soup))


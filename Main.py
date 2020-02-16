from bs4 import BeautifulSoup as soup
import time
import random
import requests
import csv

my_url = 'https://www.totaljobs.com/jobs/software-developer?s=header'
user_agent_array = ["Mozilla/5.0 (Linux; Android 6.0.1; SM-G532M Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.14.2987.98 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; P1 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Crosswalk/23.53.589.4 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'"]
index = 0
job_url = [] 

s = requests.Session()

def Update_Index(index):
    if index == len(user_agent_array)-1:
        index = 0
    else:
        index += 1
    print(index)
    return index


def Prepare_Page(url):

    r = s.get(url, headers={'User-Agent': user_agent_array[0]})
    time.sleep(random.randrange(5))
    response = r.text
    html = response
    page_soup = soup(html, "html.parser")
    return page_soup

def jobsite_Job_Info(page_soup):
    job_info = []
    try:
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
    except:
        print("Iregular format")

    return job_info

def Find_All_Jobs():
    for job_titles in page_soup.findAll("div",{"class": "job-title"}): #  finds all div section with the class of job titles
        temp_a_link = job_titles.find("a", href = True) # Gets all <a> link tags that contain the links
        job_url.append(temp_a_link.get('href')) #Stores the links in the array

def All_Job_Basic_Info():
    job_info_array = []
    for url in job_url: 
        print("\n")
        page_soup = Prepare_Page(url)
        job_info_array.append(jobsite_Job_Info(page_soup))
    return(job_info_array)

def Write_CSV_File(job_info_array):
    with open('job_description.csv', 'w', newline='') as csvfile:
        for job_descrip in job_info_array:
            jobwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            jobwriter.writerow(job_descrip)
        print("I ran")


page_soup = Prepare_Page(my_url)
Find_All_Jobs()
print(job_url)
job_info_array = All_Job_Basic_Info()
print(job_info_array)
Write_CSV_File(job_info_array)


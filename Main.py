from bs4 import BeautifulSoup as soup
import time
import random
import requests
import csv
import os.path

my_url = 'https://www.totaljobs.com/jobs/software-developer'
#my_url = "https://www.milkround.com/jobs/software-engineer"
def Page_Seach(my_url):

    user_agent_array = ["Mozilla/5.0 (Linux; Android 6.0.1; SM-G532M Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.14.2987.98 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.2; P1 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Crosswalk/23.53.589.4 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"]
    job_url = [] 
    index = 0

    s = requests.Session()
    """
    def Update_Index(index):
        if index == len(user_agent_array)-1:
            index = 0
        else:
            index += 1
        return index
    """

    def Prepare_Page(url):
        index = random.randrange(len(user_agent_array)-1)
        r = s.get(url, headers={'User-Agent': user_agent_array[(index)]})
        time.sleep(random.randrange(2))
        response = r.text
        html = response
        page_soup = soup(html, "html.parser")
        return page_soup

    def jobsite_Job_Info(page_soup):
        
        try:
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
            job_info.extend((job_title, job_salary,job_location, job_company, job_type, date_posted))
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
        type_of_edit = ""
        if os.path.isfile('job_description.csv'):
            type_of_edit = "a+"
        else:
            type_of_edit = "w"

            print("Let's create a site")
        with open('job_description.csv', type_of_edit, newline='') as csvfile:
            for job_descrip in job_info_array:
                jobwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                jobwriter.writerow(job_descrip)

    def Next_Page(page_soup):
        next_page_link = page_soup.find("a", {"class": "page-link"}).get("href")
        print(next_page_link)
        return next_page_link
        

    print(index)
    page_soup = Prepare_Page(my_url)

    Find_All_Jobs()
    print(job_url)
    job_info_array = All_Job_Basic_Info()
    print(job_info_array)
    Write_CSV_File(job_info_array)
    link_extension = Next_Page(page_soup)
    return(link_extension)

next_page_url = my_url + Page_Seach(my_url)
next_page_url = my_url + Page_Seach(next_page_url)
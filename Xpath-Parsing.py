import urllib.request as uReq
from bs4 import BeautifulSoup as BS


url = 'https://www.totaljobs.com/job/software-developer/oscar-associates-uk-limited-job89574381?src=search&page=1&position=1&WT.mc_id=A_PT_CrossBrand_Jobsite&searchCriteria=Software+Developer&searchLocation=&source=jobsite'
print("I got here")

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
request = uReq.Request(url,headers={'User-Agent': user_agent})
response = uReq.urlopen(request)
html = response.read()
page_soup = soup(html, "html.parser")


def jobsite_Job_Info(page_soup):
    job_info = []
    
    job_title = page_soup.find("div",{"class": "row title"})
    print(job_title)
    job_location = page_soup.find("li", {"class": "location icon"})
    print(job_location)
    job_salary = page_soup.find("li",{"class": "salary icon"})
    print(job_salary)
    job_company = page_soup.find("li",{"class": "company icon"})
    print(job_company)
    job_type = page_soup.find("li",{"class": "job-type icon"})
    print(job_type)
    date_posted = page_soup.find("li",{"class": "date-posted icon"})

    job_info.extend((job_title, job_salary, job_company, job_type, date_posted))
    return job_info
print(jobsite_Job_Info(page_soup))







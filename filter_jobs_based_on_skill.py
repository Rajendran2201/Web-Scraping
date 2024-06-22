'''

Refernce Wbsite: www.timesjobs.com

Problem Statement: 

Write a code to get a skill from the user and sort out the job requirements 
which requires that specific skillset and create a folder 
which contains the files of the job details reuiring the skill

'''

from bs4 import BeautifulSoup
import requests, os

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml')

job_cards = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

skill = input("Enter your skill: ")

for index,job in enumerate(job_cards):
  company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
  job_role = job.find('strong', class_ = 'blkclor').text.strip()
  skills = job.find('span', class_ = 'srp-skills').text.replace(' ','').strip()
  published_date = job.find('span', class_ = 'sim-posted').text.strip()

  if skill in skills: 
    skill_dir = f'job-posts/{skill}'
    os.makedirs(skill_dir, exist_ok=True)
    with open(f'{skill_dir}/{index}.txt', 'w') as file:
        file.write(f"Company Name: {company_name}")
        file.write(f"\nJob Role: {job_role}")
        file.write(f"\nSkills Required: {skills}")
        file.write(f"\nPublished Date: {published_date}")

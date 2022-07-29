import requests
from bs4 import BeautifulSoup

LIMIT = 50
INDEED_URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(INDEED_URL)
    soup = BeautifulSoup(result.text,"html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.find("span").string))
    maxPage = pages[-1]
    return maxPage

def extract_indeed_jobs(last_pages):
    jobs = []
    # for page in range(last_pages):
    result = requests.get(f"{INDEED_URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "resultWithShelf"})
    for result in results:
        title = result.find("h2", {"class": "jobTitle"}).string
        print(title)
    return jobs
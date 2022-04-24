import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulStoneSoup

indeed_result = requests.get
("https://www.indeed.com/jobs?as_and=python&limit=50")


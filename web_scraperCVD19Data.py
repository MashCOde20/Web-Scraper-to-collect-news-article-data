#Project scrapes data on ny times site and return title and body of article

#Imports beautiful soup and request library
import contextlib
import requests
from bs4  import BeautifulSoup

#Stores URL in url variable
site_url ='https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html'




#get request of site

response = requests.get(url=site_url)
data = response.text




soup = BeautifulSoup(data, "html.parser")
soup.prettify()
title = soup.find(name="h1", id="main-content")
print(title.getText())
print(contextlib.getText())


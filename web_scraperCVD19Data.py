# Project scrapes data on NY Times site and returns title and body of the article

# Imports beautiful soup and requests library
import requests
from bs4 import BeautifulSoup

# Stores URL in site_url variable
site_url = 'https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html'

# Get request of site
response = requests.get(site_url)

# Check if the request was successful
if response.status_code == 200:
    data = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(data, "html.parser")

    # Extract title
    title = soup.find(name="h1")
    if title:
        print("Title:", title.get_text())
    else:
        print("Title not found.")

    # Extract article body
    paragraphs = soup.find_all('p')
    body = ' '.join([para.get_text() for para in paragraphs])
    
    # Print the body of the article
    print("Body:", body)
else:
    print("Failed to retrieve the page. Status code:", response.status_code)

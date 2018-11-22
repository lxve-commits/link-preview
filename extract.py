import requests
from bs4 import BeautifulSoup


def getLinks(html, headers):
    """Extract links from url."""
    r = requests.get(html, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.select('.post-content p > a')
    return links
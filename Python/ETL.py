from bs4.element import SoupStrainer
import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
titres_from_soupe = soup.find_all("a", class_="gem-c-document-list__item-title")
titres = []
for titre in titres_from_soupe: 
    titres.append(titre.string)
print(titres)
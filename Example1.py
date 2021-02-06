import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')

soup = bs4.BeautifulSoup(res.text,"lxml")

# selecting all the items with the class "toctext"
soup.select(".toctext")
for item in soup.select(".toctext"):
    print(item.text)


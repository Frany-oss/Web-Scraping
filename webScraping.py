import requests
import bs4

# Extracting the html from a web page
res = requests.get("http://www.example.com")

# Grabbing and analyzing information 
soup = bs4.BeautifulSoup(res.text,"lxml")
print(soup)

# Now let's use the .select() method to grab elements. We are looking for the 'title' tag, so we will pass in 'title'
title_tag = soup.select('title')

# Extracting "<title> ....... </title>"
print(title_tag[0])
# Extracting the information inside the tag
print(title_tag[0].getText())




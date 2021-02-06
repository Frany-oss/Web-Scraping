import requests
import bs4

# Get title of every book with a 2 start rating

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
# basse_url.format('20') -> goes to page 20

# res = requests.get(base_url.format('1'))
# soup = bs4.BeautifulSoup(res.text,"lxml")

# products = soup.select(".product_pod")
# example = products[0]
# example.select('a')[1]['title'] # grabbing the second 'a' because there is the title

# We can check if something is 2 starts
# example.select('a')[1]['title'] to grab the title

two_star_titles = []

for n in range(1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)

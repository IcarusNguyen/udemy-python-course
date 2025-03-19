import requests, bs4

# res = requests.get('https://quotes.toscrape.com/')
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# authors = {name.text for name in soup.select('.author')}
# quotes = [quote.text for quote in soup.select('.text')]
# tags = [tag.text for tag in soup.select('.tag-item')]
authors = set()
page_still_valid = True
page = 1

while page_still_valid:
    url = f'https://quotes.toscrape.com/page/{page}'
    res = requests.get(url)
    if 'No quotes found!' in res.text:
        break
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    for name in soup.select('.author'):
        authors.add(name.text)
    page += 1

print(*authors, sep='\n')
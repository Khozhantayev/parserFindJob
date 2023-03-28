from bs4 import BeautifulSoup
import requests

x = 0
while True:
    if x == 0:
        url = 'https://news.ycombinator.com/jobs'
    else:
        url = 'https://news.ycombinator.com/jobs' + all

    request = requests.get(url)

    soup = BeautifulSoup(request.text, 'html.parser')

    themes =soup.find_all('td', class_='title')

    for theme in themes:
        theme = theme.find('a')
        if theme is not None and 'Python' in theme.text:
            print(theme.text)
            print('===')

    next = soup.find(class_='morelink')
    nextlink = next.get('href')

    all = nextlink[4:]

    x = x + 1

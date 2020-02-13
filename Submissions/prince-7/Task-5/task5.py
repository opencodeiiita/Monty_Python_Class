import requests
from bs4 import BeautifulSoup

Source = 'https://m.imdb.com/chart/top/?ref_=nv_mv_250'
page = requests.get(Source)

soup = BeautifulSoup(page.text, 'html.parser')

page=[]
i=1
section = soup.find('section', { 'id': 'chart-content' })
for div in section.find_all('div', {'class': 'col-xs-12'}):
    span = div.find('span', {'class': 'media-body'})
    head = span.find('h4').text.split("\n")[2]
    rating = float(span.find('span', {'class': 'imdb-rating'}).text)
    if(rating>8.5):

        print(i,".",head)
        print("IMDB-Rating:",rating)
        print("\n")
        i+=1 


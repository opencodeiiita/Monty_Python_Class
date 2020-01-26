import requests
from bs4 import BeautifulSoup

# get the data
data = requests.get('https://m.imdb.com/chart/top/?ref_=nv_mv_250')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

data = []
section = soup.find('section', { 'id': 'chart-content' })
for div in section.find_all('div', {'class': 'col-xs-12'}):
    span = div.find('span', {'class': 'media-body'})
    head = span.find('h4').text.split("\n")[2]
    star = float(span.find('span', {'class': 'imdb-rating'}).text)
    if(star>8.5):
        print(head, " - Rating: ",star)
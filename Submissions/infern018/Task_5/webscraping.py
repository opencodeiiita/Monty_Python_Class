import requests
from bs4 import BeautifulSoup

URL = 'https://m.imdb.com/chart/top/?ref_=nv_mv_250'
page = requests.get(URL)#linking the webpage

soup = BeautifulSoup(page.text, 'html.parser')#fetching the data

page=[]
i=1
section = soup.find('section', { 'id': 'chart-content' })
for div in section.find_all('div', {'class': 'col-xs-12'}):#navigating through particular html classes
    span = div.find('span', {'class': 'media-body'})
    head = span.find('h4').text.split("\n")[2]
    rating = float(span.find('span', {'class': 'imdb-rating'}).text)#finding for particular imdb(only >8.5)
    if(rating>8.5):

        print(i,".",head)
        print("IMDB-Rating:",rating)
        print(" ") 
        i+=1
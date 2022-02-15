
from selenium import webdriver 
from bs4 import BeautifulSoup as bs 
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.melon.com/chart/index.htm')

html = driver.page_source
soup = bs(html)


song_data = []
rank = 1

songs = soup.select('tr.list50')

for song in songs:
  title = song.select('p.title > a')[0].text.strip()
  singer = song.select('p.artist > a')[0].text.strip()
  singer_name = singer[0:len(singer)//2]
  song_data.append([rank, title, singer_name])
  rank += 1

import pandas as pd

df = pd.DataFrame(song_data,columns= ['순의','타이틀','가수'])
df
df.to_excel('Melon.xlsx',index=False)
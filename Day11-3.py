




import requests
from bs4 import BeautifulSoup as bs
import pandas 
html = requests.get('https://music.bugs.co.kr/chart')  
soup = bs(html.text)
len(soup.select('tr')) 
songs = soup.select('table.byChart > tbody > tr')  # -> 최종 100 추출 완료
songs[0]
song_data = []
rank = 1

songs = soup.select('table.byChart > tbody > tr')  # -> 최종 100 추출 완료

for song in songs:
  title = song.select('p.title > a')[0].text
  singer = song.select('p.artist > a')[0].text
  song_data.append([rank, title, singer])
  rank += 1

song_data

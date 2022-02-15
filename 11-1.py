# pip install requests
import requests  # 웹 페이지 연결 모듈
# pip install bs4
from bs4 import BeautifulSoup as bs # 읽어온 웹페이지를 분석하기 쉽게 정제 모듈
import pandas  # 데이터 분석 모듈
html = requests.get('https://music.bugs.co.kr/chart')   # 웹 페이지 코드 읽어오기

#print(html.text)
soup = bs(html.text)  # BeautifulSoup 을 통해 데이터를 분석하기 용이하게 정제한다. 
# print(soup)
len(soup.select('tr'))  # tr태그가 붙은 부분들을 모두 추출
len(soup.select('tbody > tr')) # 원하는 100개 아니므로 범위를 축소
len(soup.select('table.byChart > tbody > tr'))  # 원하는 100개 아니므로 범위를 축소
songs = soup.select('table.byChart > tbody > tr')  # -> 최종 100 추출 완료
songs[0]
len(songs[0].select('p > a'))
len(songs[0].select('p.artist > a'))
singer = songs[0].select('p.artist > a')[0].text
singer
songs[0]
len(songs[0].select('a'))
len(songs[0].select('p.title > a'))
title = songs[0].select('p.title > a')[0].text
title
song_data = []
rank = 1

songs = soup.select('table.byChart > tbody > tr')  # -> 최종 100 추출 완료

for song in songs:
  title = song.select('p.title > a')[0].text
  singer = song.select('p.artist > a')[0].text
  song_data.append([rank, title, singer])
  rank += 1

song_data
import pandas as pd

df = pd.DataFrame(song_data, columns = ['순위','타이틀','가수'])
df
df.to_excel('bugs.xlsx', index=False)



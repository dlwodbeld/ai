#pip install selenium
from selenium import webdriver #파이썬으로 웹 브라우저 컨트롤
import requests
from bs4 import BeautifulSoup as bs #분석을 용이하게 정제

import pandas #데이터 분석 모듈
driver = webdriver.Chrome('chromedriver.exe')
html = driver.get('https://www.genie.co.kr/chart/top200')
soup = bs(html.text)
song_data = []
rank = 1

songs = soup.select('table.byChart > tbody > tr')  # -> 최종 100 추출 완료

for song in songs:
  title = song.select('p.title > a')[0].text
  singer = song.select('p.artist > a')[0].text
  song_data.append([rank, title, singer])
  rank += 1

song_data

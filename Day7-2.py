"""
# urllib 크롤링 등 웹 접근 라이브러리

from urllib import request

target = request.urlopen('https://www.naver.com')
output = target.read()

print(output)
"""

"""
# 외부모듈
# 파이선이 기본적으로 제공하는 것이 아니라 누군가가 만들어서 배포하는 모듈을 말한다.

!pip install pybithumb

import pybithumb
import time
print(pybithumb.get_current_price('BTC'))
while True:
    print(pybithumb.get_current_price('ETH'))
    time.sleep(1)

tickers = pybithumb.get_tickers()

for tickers in tickers:
    price = pybithumb.get_current_price(ticker)
    print(ticker,price)
    time.sleep(1)


print(pybithumb.get_markey_detail(BTC'))
#저가,고가,평균 거래량

price = pykorbit.get_current_price('BTC')
price = pybithumb.get_current_price('BTC')



"""

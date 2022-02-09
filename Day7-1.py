'''
검색하고 있는 데이터가 존재하지 않는경우
현재 찾는 데이터가 존재하지 않는 경우 무한루프가 발생한다.

탐색 데이터가 발견되지 않으면 k값을 점점 증가하다가 다시 처음부터 검색하고 이 과정이 계속 반복된다.
그러면 과연 어디까지 찾아야 존재하지않는다고 할까
바로 데이터가 보관되지 않는 요소9값이 0인 요소)가 나왔을떄다.

만약 데이터가 존재한다면 설사 저장할 떄 충돌이 발생하여 어딘가 다른 요소에 저장되어있다 하더라도
저장 위치를 찾을 떄까지의 사이에 데이터가 0인 요소는 절대 있을수 없다.
https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Day7-1.drawio#R3Vpbj6M2FP4tfbDUPnTEPeYxJOlupa000qjabl9WBJzAhuAInEnSX99jbCDgSYadScaZeUnsg43Nd75z8QFkT9b7T0W4Sf6iMcmQZcR7ZE%2BRZY18D3654CAEjmcIwbJIYyEyW8FD%2Bh%2BRwnrYNo1J2RnIKM1YuukKI5rnJGIdWVgUdNcdtqBZd9VNuCSK4CEKM1X6NY1ZIqTYGrXyzyRdJvXKpueLK%2BuwHiyfpEzCmO6ORPYM2ZOCUiZa6%2F2EZBy7Ghcx748TV5uNFSRnQyY47r9%2Fl5%2FoN%2Fadkf2PP6Ovy%2Fv0d8sRt3kMs618YrlbdqghIDEgIru0YAld0jzMZq00KOg2jwlfx4BeO%2BYLpRsQmiD8QRg7SPWGW0ZBlLB1Jq%2BKNflCJx9Oikq6LSJy5onkA7GwWBJ2ZpzpNjoA7hK6Jqw4wMSCZCFLH7sbCSWLls24FmhoSKx%2FAncV9gfYMVOxzzJgOsd4l6SMPGzC6uF3YGtdBBdplk1oRotqnh2HBC8ikJesoCtydMWLMJkvGswfSQHbOo%2B6CpKcYBmS27Vxy%2B6utRSzpn9yZCX1uIvDOlJgPYDz0EDokmtzzP0PCHKak8uS3HReSV459Z6msHSrT6%2BrT9fqKUpYlZzV01WzjZerr17uSH85fef%2BCA%2F1RyOd%2FggrwEPw%2FIzcYIXcKQj2ihaKhK7n2%2FJ5z3QFP2N7uh2N%2F9HCZp1vPc9TSydPTdVDrKBbtYAtnAMQ1w3TVNTRgm1q4WzT18ZZUyWtpuh4Sd5aA3mLddK2vvFHCmyDkTe1Ql9v80Ros4xfhPMwFHUMjnC93HuBIxI9mXvPseu4xpX8C9btXyz3wwVFdyjFjad19UYUfwL42QQFBgpmvOFPEXZ4bJyNudC3RKy8sQDZkFUfgb0PR%2BCh1RDL1krgJ6pQwNuxgcCpcQLP0NitGhPOZM5tH%2FkYzQKEx8jn3F7xTmAhjKuZmBNdzMRuNS6oLlWNsXN3c%2Bx3tbPfVNmvKT0keXy90sng8%2FjblFgco6dP8QBKieX2ajVafCPZp%2Byfo%2FY3fqs7V%2Fame3nnqnOQnUv609cWaYbpsuk%2Fo0uwkvBwNGzDB5Sn13H7TscxznKsP77eV0slsYOLEstUi7gr%2BPsVzvmB%2BRuc72%2FgcG%2BfMj59uYuK2nvPXYZ66lfnLi%2ByJbNnG55x3pb6Nt4bfyVbUuu6e54EQTYVTKoTgXJMgAYkSpBciav%2BCGGvEsLZYVAmVSbhhjdjGm3XldafM8i5YN2XudYDtXNzJm0ryoPMSLXqd%2FWK0LO1w6raxDU4fAHsXGfUpaR26Aa89hBsqr%2BVsHqvRSWu6%2F2Sfy1yt8joLkrCgt1lEGG%2BZ%2Bk6PYX1BfD0RjeGZ20L5%2FB8y%2FdsjtU1VlM7QGrd%2FOX%2B7woWqR8gawCD3jg59vBINypq5GxrnyLTCRyZ4PSLTAHyjaq2BBKPD5NVJFFXGvHBMjNyeU7UlKD4%2FS0UTKtL1VqngkoUZhndDogpG1KkAAgp2kn3regifO6d74Z%2BwIOvpjm1Enj8tkYkpL5QASA%2Frct8lUJnVQIb1HXuRlM%2FoeJGm7WuO8nyFPk%2B17tcEV9dxRtapiylOahweqE01%2B7luYPfS79A59Btv28UZ5r2I1F79j8%3D


#예외 처리고급
프로그램을 개받ㄹ하다 보면 수많은 오류를 만나게된다. 또한 처음 프로그램을 개발했을때
모든 오류를 예측하고 처리할 수는 없다. 개발이 완료된 후에도 예측하지 못한 오류들이 계속 발생되기때문에
유지보수가 필요하다.

try:
    예외발샐 가능성 있는 구문
except:
    에외가 발생했을때 실행할 구문

try:
    예외발샐 가능성 있는 구문
except 예외의 종류 as e(예외 객체를 활용할 변수 이름):
    에외가 발생했을떄 실행할 구문.

예외가 발생하면 예외 정보가 생기고 예외 정보는 예외 객체에 저장되어 생성된다.

#예외 객체
try:
    num = int(input('정수를 입력하세요'))
    print('입력한 정수:',num)
except Exception as e:
    print('type(exception) : ',type(e))
    print('exception : ',e)

만약 큰 규모의 웹 서비스를 구축하게 된다면 다양한 예외가 분명히 발생한다.
예외가 발생할떄 그 정보를 수집하면 이후 프로그램을 유지/보수하는데 큰 도움이 된다.

# 예외 구분하기

list = [52,273,32,72,100]

try:
    num = int(input('정수입력 : '))
    print(f'{num}번째 요소 : {list[num]}')
"""
------무슨에러든 다 처리하는코드-----
except Exception as e:
    print('type(exception) : ',type(e))
    print('exception : ',e)

"""
코드 내부에서는 이처럼 여러가지의 예외가 발생할 수 있다.
파이썬은 예외들을 구분하여 처리할 수 있다.
"""
----따로따로 애러 처리방법----
except VealueError:
    print('정수를 입력하셔야만 합니다.')
except IndexError:
    print('리스트 크기보다 큰 수는 입력하실수 없습니다.')
"""
"""
----애러객체내용도 확인하는방법----
except VealueError as e:
    print('정수를 입력하셔야만 합니다.')
    print('exception',e)
except IndexError as e:
    print('리스트 크기보다 큰 수는 입력하실수 없습니다.')
    print('exception',e)
"""
------파악하지못한 에러 예외처리------
list = [52,273,32,72,100]

try:
    num = int(input('정수입력 : '))
    print(f'{num}번째 요소 : {list[num]}')
    애러발생() #진입은 가능한데 애러가 발생한다.
except VealueError as e:
    print('정수를 입력하셔야만 합니다.')
    print('exception',e)
except IndexError as e:
    print('리스트 크기보다 큰 수는 입력하실수 없습니다.')
    print('exception',e)
except Exception as e:
    #나머지 모든 예기치못한 예외를 여기서 처리한다.
    print('미리 파악하지 못한 예외 발생')
    print(type(e),e)

--너무 치명적인 문제인데도 프로그램 강제 종료되지 않게 만들면 그것으로 또다른
커다란 문제가 될수있으므로 상황에 맞게 대처할수 있어야한다.

큰 규모의 프로그램을 개발할떄는 '예외처리로 떡칠한다'고 표현할 정도로 예외처리를
많이 사용하게된다.
예외처리에서 가장 중요한것은 '이코드에서 어떤 예외가 발생할것인가?'를 미리 잘 예측하는것이다.
# 예외를 강제로 발생시키기. raise

num = int(input('정수입력 >>>'))

if num > 0:
  raise NotImplementedError
else:
  raise NotImplementedError
# 모듈
# 여러 변수와 함수를 가지고 있는 집합체
# 파이썬에 기본적으로 내장되어 있는 모듈을 '표준 모듈'이라고 부르고
# 다른 사람이 만들어서 공개한 모듈을 '외부 모듈'이라고 부른다. 
# math 모듈 - 수학과 관련된 기능들을 가진 모듈

import math

print(math.sin(1))
print(math.cos(1))
print(math.tan(1))

# ceil() 올림
# floor() 내림
# round() 반올림
#from math import sin, cos, tan
from math import *

print(sin(1))
print(cos(1))
print(tan(1))

import math as m
print(m.sin(1))
print(cos(1))
print(tan(1))


#!pip install selenium
import selenium
'''
"""
import selenium
# random 모듈 - 랜덤한 숫자를 생성해주는 모듈
import random

print('# random 모듈')

# 기본적으로 0.0 에서 1.0 사이의 float  으로 난수를 발생시킨다. 
print(' - random() : ', random.random())


# uniform(min, max) : 지정한 범위 사이의 float을 발생시킨다. 
print(' - uniform(10,20) : ', random.uniform(10,20))


# randrange() : 지정함 범위의  int 를 발생시킨다. 
print(' - randrange(10,20) : ', random.randrange(10,20))
print(' - randrange(10) : ', random.randrange(10))

# choice(list):  리스트 내부에 있는 요소를 랜덤하게 선택한다. 
print(' - choice([1,2,3,4,5]) : ', random.choice([1,2,3,4,5]))


# sample(list, k=숫자) : 리스트의 요소 중 k개를 랜덤하게 뽑아준다.
print(' - sample([1,2,3,4,5], k=2) : ', random.sample([1,2,3,4,5], k = 2))


# shuffle(list) : 리스트의 요소들을 랜덤하게 섞어준다.  
# shuffle은 파괴적 처리를 하기 때문에 먼저 섞는 작업을 하고 나서 출력한다. 
list = ['1','2','3','4','5']
# print(' - shuffle([1,2,3,4,5]) : ', random.shuffle(['1','2','3','4','5']))
random.shuffle(list)
print(' - shuffle([1,2,3,4,5]) : ', list)
"""
"""
# 여러분은 로또 당첨 번호 추천 인공지능 시스템을 개발하였다. 
# 매주 5개의 1등 완전 당첨 추천 번호 판매를 시작한다.
# 실행하면 5개의 로또 번호 세트를 보여주는 프로그램을 작성하시오. 

# 
li = [0,0,0,0,0,0]
for i in range(5):
    for j in range(6):
        li[j] = random.randrange(1,47)

    print(li)
    li = [0,0,0,0,0,0]

"""

"""
# os 모듈

import os

print('현재 운영체제',  os.name)
print('현재 작업폴더',  os.getcwd())
print('현재 폴더내부',  os.listdir())

#os.mkdir('hello2')
print('현재 폴더내부',  os.listdir())
os.rmdir('hello')
os.rmdir('hello2')
print('현재 폴더내부',  os.listdir())
"""

import datetime

now = datetime.datetime.now()
"""
print(now)
print(now.year,"년")
print(now.date,"월")
print(now.day,"일")
print(now.hour,"시간")
print(now.minute,"분")
print(now.second,"초")
"""
"""
if now.hour < 12:
    print(f'현재 시각은 {now.hour}시{now.minute}분 오전입니다.')
else :
    print(f'현재 시각은 {now.hour}시{now.minute}분 오후입니다.')

"""

if 3 <= now.date <=5 :
    print(f'이번달은 {now.date}월로 봄입니다.')
elif 6<= now.date <=8 :
    print(f'이번달은 {now.date}월로 여름입니다.')
elif 9<= now.date <=11 :
    print(f'이번달은 {now.date}월로 가을입니다.')
else :
    print(f'이번달은 {now.date}월로 겨울입니다.')
'''
number = input('정수를 입력하세요.')

if number[-1] in "02468":
    print('짝수입니다.')
if number[-1] in "13579" :
    print('홀수입니다.')
'''



# pass
'''
number = input('정수를 입력하세요.')
if number > 0:
    pass
else:
    pass
'''

# 리스트와 반복문
'''
li = [1,2,3,4,5] #여러개위 데이터를 저장하여 사용한다.

for i in li:
    if i >=3:
        print(i)
'''


# 딕셔너리와 반복문
# for : 반복횟수를 정확히 알고 있을떄 주로 사용
# while : 반복횟수를 정확히 알수없을떄 주로 사용
'''
dict = {
    1:'홍길동',
    2:'이몽룡',
    3:'놀부',
    4:'수월가',
    5:'도화전'
}
#print(dict[1])
for i in dict:
    print(i,dict[i])

#list(range(5)) #시작을 생략하면 0부터 5미만까지
#list(range(0,5,2))

print(list(range(0,5,2)))
'''
'''
for i in range(3):
    print(f'{i}번째 반복')
i = 0
while i < 3:
    print(f'{i}번째 반복')
    i += 1
for i in range(2,-1,-1):
    print(f'{i}번째 반복')
'''

# break 반복을 중지하고 나옴. 
'''
i = 0
while True:
    print(f'{i}번째 반복입니다.')
    i +=1

    inp = input('종료할까요(y) >>')
    if inp in ['Y','y']:
        print('반복을 종료합니다.')
        break
'''

# continue 반복을 중지하고 다음반복으로 넘어가는것
'''
num = [1,2,3,4,5,6,7,8,9]
for num in range(1,11):
    if num % 2 == 0:
     continue
    print(num)
'''

# enumerate()
# 0번진구
# 1번 철수
# 2번 미애
# 3번 마야
# 4번 현수
'''
student = ['진구','철수','미애','마야','현수']
no = 0
for i in student:
    print(f'{no}번 {i}')
    no += 1
'''
'''
student = ['진구','철수','미애','마야','현수']

no = 0
for no,i in enumerate(student):
    print(f'{no+1}번 {i}')
'''

# items() 딕셔너리는 itmes() 함수를 사용하여 key와 value 값을 한번 추출할수있다.
'''
dict = {
    '홍길동':185,
    '이몽룡':189,
    '선춘향':168
}

for name,height in dict.items():
    print(f'{name}의 키는 {height}입니다.')
'''

# array[]리스트 내포
'''
array = []

for i in range(0,20,2):
    array.append(i)
print(array)

array = [i for i in range(0,20,2)]
print(array)
'''

array = ['사과','체리','바나나','과자']

output = [ i  for i in array]
output1 = [ i  for i in array   if i !='과자'] 

print(output)
print(output1)

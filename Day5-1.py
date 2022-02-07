'''
function 함수만들기

수학에서의 함수와 유사
input -> 함수 ->output

def 함수명(변수):

'''

from re import I
import re
from unittest import result


def print_3(val,n):
    for i in range(n):
        print(val)

print_3('hi',5)
print_3('hello',2)
'''
가변 매개변수
함수를 선언할 때 매개변수와 함수를 호출할 때 매개변수가 같아야만햇다. 적어도 안되고 많아도 안된다.
'''
'''
def print_n_times(n,*val):
    for i in range(n):
        for v in val:
            print(v)
        print()

print_n_times(3,'hi','hello','good morning')

def sum_all(*val):
    print(sum_all(val))
sum_all(1,2,3,4,5)
sum_all(3,4)

def print_n_times(n,*args):
    for i in range(n):
        for v in args:
            print(v)
        print()

def return_test():
    print('A위치입니다.')
    return
    print('B위치입니다.')
return_test()
'''
def sum_all(start,end):
    output = 0
    for i in range(start,end+1):
        output += i
    return output

print(sum_all(0,100))

#재귀함수(사용권장은 안함)
def hello():
    print('hi')
    return hello()
hello

def facto(n):
    output = 1
    for i in range(1,n+1):
        output *= i
    return output
print(facto(3))
print(facto(6))

#피보나치수열(토끼번식)
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))

#튜플과 함수
#튜플은 함수의 리턴에 많이 사용된다.
#리턴하고 할당 할 수 있기때문이다.

def test():
    return 10,20 #튜플의 (소)괄호는 생략도 가능하다.
a,b = test()

# 함수의 종류 4가지
'''
input 도 있고 ouput 도 있는 함수 (*****)
input 은 없고 output 은 있는 함수
input 은 있고 output 은 없는 함수
input 도 없도 output도 없는 함수

# 1 input 도 있고 ouput 도 있는 함수 (*****)
def add(a,b):  
  return a+b

print(add(1,2))

#2 input 은 없고 ouput 은 있는 함수 (*****)
def say():  
  return 'hi'

print(say())

# 3 input 은 있고 output 은 없는 함수

def add(a,b):
  print('%d, %d의 합은 %d입니다.' % (a, b, a+b))

add(3,4) 

# 4. input 도 없도 output도 없는 함수
def say():
  print('hi')
  print('hi')
  print('hi')

say()

'''
def add_mul(choice,*args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * 1
        return result

print(add_mul('add',1,2,3,4,5))
print(add_mul('mul',1,2,3))

def say_myself(name,old,man=True):
    print('나의 이름은 %s 입니다.'%name)
    print(f'나의 이름은 {name} 입니다.')
    print('나의 나이는 %d 입니다.'%old)
    print(f'나의 나이는 {old} 입니다.')

say_myself('박응용',27)

#지역변수 local variable 와 전역변수 golbal variable
#함수 안에변수랑 밖에변수랑 다른거다.
a = 1
def vartest(a):
    a = a + 1
vartest(a)
print(a)
    
#lambda 를 사용하면 코드를 더 깔끔하게 작성할 수있고 코드의 복잡성을 줄여준다.
#재 사용성은 상당히 떨어진다.

#def add(a,b):
#   return a+b
add = lambda a,b:a+b
print(add(3,4))

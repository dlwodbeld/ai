"""if조건문
조건에 따라 특정코드를 실행하거나  특정 코드를 실행하지 않게 만들고 싶을떄 사용.
코드의 실행 흐름을 변경시키는 것을 조건분기라고 부른다.

"""

num = int(input('정수를 입력하세요 : '))

if num > 0:
    print('양수입니다.1')

if num < 0:
    print('음수입니다.1')

if num == 0:
    print('0입니다.1')

if num > 0:
    print('양수입니다.2')
elif num<0:
    print('음수입니다.2')
else :
    print('0입니다.2')
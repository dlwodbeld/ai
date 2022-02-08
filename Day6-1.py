'''
Linear Search 선형 탐색법

보관된 데이터를 맨앞부터 순서대로 원하는 값을 찾을때까지 탐색한다.
탐색 처리는 반복구조를 사용하여 기술한다.
반복구조에서는 종료조건을 잊지 말자.

첨자(index) 0 1 2 3 4
데이터      4 2 3 5 1   찾을 데이터 : 5

'''

arr = [4,2,1,5,3]
for i in range(0,5):
    if arr[i] == 5:
        print(f'{i+1}번째에 요소가 일치')
        break
    else:
        print('찾지 못했습니다.')
def linear_search(no,list):
    for i in range(len(list)):
        if no == list[i]:
            print(f'{i}번째 요소가 일치')
            return i
    return 
print(linear_search(5,[4,2,3,5,1]))

'''
Binary Search 이진 탐색법
이진탐색법은 탐색하는 범위를 절반씩 줄여서 탐색하는 방법이다.
데이터들이 먼저 오름차순이나 내림차순으로 정렬되어있어야만 쓸수있다.

# https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Day6.drawio#R7V1Zc6M4EP411O4%2BJIUECHj0kd15mKmaqnmY2actbIjNLjYpjCfJ%2FPqVOHyo5VgeHy2YvCQgDkN3q4%2BvW43ljBYvfxXR0%2FxTHieZRe34xXLGFqV%2ByPhfMfBaD7jMrgdmRRrXQ2Q78CX9kTSD7WnrNE5WeyeWeZ6V6dP%2B4DRfLpNpuTcWFUX%2BvH%2FaY57t%2F%2BpTNEvAwJdplMHRr2lczuvRgPrb8Q9JOpu3v0xYWB9ZRO3JzZus5lGcP%2B8MOQ%2BWMyryvKy3Fi%2BjJBO0a%2BlSX%2FfngaObByuSZalzQTpyBj%2B%2BfXI%2BROsX8sS8r3fl%2Bo407%2FE9ytbNGzdPW762JEhiTpFmNy%2FKeT7Ll1H2sB0dFvl6GSfid2y%2Btz3nY54%2F8UHCB%2F9NyvK1YW%2B0LnM%2BNC8XWXO0%2Fk3xQwdfrhla5etimrz1Ro2QRMUsKd86j254wGU3yRdJWbzyC4ski8r0%2B%2F6DRI0UzTbnbQnNNxpan0J3QPbIehhZYWgFnIv2xHoYWgPPGvK729WBByvwqkFbjMss2jJAUPN5npbJl6eootMzn5YqYn9PijJ5eZvckDrNBW4j082kpnaz%2F7ydIqSV%2B%2FnO9Givuzw9Hadvgky1BTnAlGQK6L7ij1xC4mcZ19nJcfF8TLNslGd5UV3nxFESPE75%2BKos8v%2BSnSNsGiSTx6sINAuwBVpDnLlBeRKbcT5dL6r3PEbaSS3eHycXVAVOawob0nkUm3SuBukqWWoNOt2nUkvXxctMuDT3j1n%2BPJ1zmb7PuBr4J0sX6SFaX0ISPePoGQCCLvOOK1dPU7m6HqZu9TxA%2BVfuDP8apPcOzJMbkR5QnkcTlje0LW8sfDIxZCscsXm%2BmKxXN3HCmG2aF8ag5uUua0is0BYbQ0d4t9ybDQIrDCq3diw2aHU0GFtDuxkcutbD2ApcMSKODqyhV91kLFzkMIB0P8UBljyMx8eETZUeRuyHE9u%2BiofhYvOKKJjVbcXiayoWVL0C4%2B0euMsE3UehMKDuuDQHutKM6qFA11DGMUbWkFnh6DB2YUYYI0k0vtdNFBItTKcryPhQ2c3Qq4wjN5ROZRxHYiMIK1NLq6Ods5IOM81MQgnvuGIh2sCSg6lZ2sfcITy3kixaCDHNhJa4i84T8MtrDYoOG5Gwd%2BLq6IqriyquELCLJHGdmCauG2WL57bZvRNXV1NcUUF7AjHSiSStMCRBllYX3xeAoFCyjKHAdil0Y%2BigkQOpii96Egjvoht2t3ea0mGamtLxMVWlA3GyLiI25kE2DnRVu5%2FccHRBSAfV%2FrswuOp8Sk%2Bb9C4qAOxABNi4zJJ59T2OAoaBwFddKzWgba0UH6yBRyIQSMoqz3ZS8K2Z2KpO9gWkJvA0Vt1Bovp%2BWUBdvydEPY5W843cR1k6W%2FLtKSdvwnX3UBA%2FnUbZoDmwSOO4mi9yaUFdoUjr%2F%2BK2guD2PRObgheuuP0yL6fz5qcu4dvIliDw7z3A3kDBXeZdSx2psM6hFXDOuU1GMDjAv3BghdU5ATud2fCcsYBNa7S6%2BvV7IyUiTotkWqa5uBPXi4Jnl5YS6h%2BHtphCRoKrOcBQb3beZLm62BZqjseF0NaXDnrAcrkEvgfsalSq3dTsSxQyIOqFMUL3J7127RnDnPUeFM7uh2fatPcoqsY9VH1GzIkRQPUZurLwIESGoyySl7T8VrltXrP3986R8Utz52rndc9lu4yQn6s3mks%2F5yn%2F6S3D5dS8JzGynlTNVRIvN49xBnshENcDhaQLgnqoyXgX0r5WSNRchYSf3fRUYe07aPEzzPWZcaCFR9%2B5eyXuUobPXcUCrHfuXoS7jovOXda7cmFPN%2FvhoSaePIjidRFLCqlpWBJTWKOOS7RuBbwXoko0zEyJyve7TTlVrfn5XQA%2Fbl3VIkstflqPQSvbeXzPCzXlltlqbt1Gblkv15Zq0x61WLh9TJNrAICyQMf3WO9WLJ6tAdRIXRjI4ZQeUjcoiuh157QnccLq8O8EoeTYB1IHoiPnt8%2B1FYr6CS4KG7bvviM16WaK8a0hAUKEbZfxkSumyEy%2BR78%2FxVxig9mIHv4SAidFx1UpaddLHl8nhLyuTbGws4shMJGrBfBjYKJYM9h5sdZe%2FkZQywWIYgGcqXEwEF38QJgoVmR1PhImRDe7SQjucjjFyi6kYJgTuXjdKR4Qu383t6t2tuUD1d4V6gdOYBu9TqkBkdsAOLZeBHOpoIEouuMYF6FDNYYeopMe9pMl2p1YDvHrVkoMItGmRbpAZPFDXdLDlglUOxaiyD0%2BbBQb29bnWdvqvG2t3tXr887XEwesJgVlFNfB%2FbimkUoB94G84xfcBPnbTIN9hbjb5SBLlr9zu%2F6HWXbcgE4HrQ7sk1LUjqQpbicZCiPp36o%2BarY1fGhBVBFbV1jrwBoOW0C16qkZVM0y6wVsYqRdyfYbYKAZndeA%2BBvQe43CaLx7nT4AYfF7fRCq0eyja3pFP1o%2BV6%2F8nLV2idRR3D9irWU%2FQrrgWtYahtzGqr1VLVj2PfUuNFcd49q%2BE6oTy%2BtqwAvQSP7SAP7yROJorODsmjrThztQ6%2B42D7pD%2B3kSxUJB7Hcysyo7KGejyyjNlOcywEHkxmc%2BPkai06Ora3KuWypGHNQ6vc2D7tC%2BqXxQSe%2Fv9RyoxJuHtX9CPiFLc4Af3CpaenW%2F9LERUy2BpqgCrWj81f1U5wnUx011tg8KMluNUvHGgjo%2BVBs3RMQklRHi%2B8IOhBK7BwjIjZ9sAxzo%2FuULHaqtCXDzhe2D7gbcjRKovyBQB9Y87B7W3%2BiB3bYGIjpvgvL6wz2jKmQX3%2BgxFW8EswAfFVO0Y%2ByDQ6IdSbq4HraiD1MPHBJ96iOrIcU3ZCSHZC%2FKQfZNZFDdAOfEhZBF%2F7vcnK80DqDfEn8DKvHtQkl0GWQn9pEkuifXW596Qfsm14XxFY3Ka0hiD6nYQTAMKEsCpewm%2BASwuPBXmNRXKo250aR25b4AfZnUMPw9iJ%2FXU%2FsOf1bLRcQmzGpFjzqMaX7JKdt2udL4UiFusaGiHVcXv%2BQgt9MxoKrD718a1NOuFvNxwydFo6qepEGBoOPDlYqmuJ0XdN2WuAS3c9TmQbuaB5XF2YBEaC9bqhLtxlGEIavuHn7S4BTq45ZZKxp3GZcIlXWGAWCjondR9zKhoJ2sAalQRaOarusCph8a4tYSKvqB%2FgqpUDgN8GNJRSPLHvgkbUMlDauI28ajjx0ZT6E%2Bboyj6Ltlci5UblxmgHvCOpM2MaHTB9Neu3Q2yqVOZwSSBF0rMSO3RDyaZyH01FQOuMJ3375AfveTz99vt3il1I%2Bi66bx%2BVzQntsEvwaq6nfFdMQO%2FwKKiRBQj%2FiumTRnFARwzE9Kg3agJuim9luvaLrJ9Xe1071N31ZQfOdzUqT87UX%2F18srn3PBCL1ZQmzNL6idqlNYa7N1FQR8spv0Z2GKzkvnL%2FgGomwG1gI%2BP2vCvO8l1uLro46o31UmvilYy880xDLBS9Tn9Nkq%2FUxOQ3xZWaRRHbJrLwYR15Fx4WuuQOe7RZ6Xu6ZF9Gr%2FlMeJOON%2F
'''

'''
예외처리 (에러처리,오류처리,버그처리.....)
1.프로그램 실행 전에 발생하는 오류 - 구문오류 syntax error
2.프로그램 실행 중에 발생하는 오류 - 런타임 오류 runtime error,예외 exception
----1----
print('#예외를 강제발생')
#EOL End of Line 실행 조차 되지않는 오류
----2----
print('프로그램이 시작되었습니다.')
list[0]


'''
"""
num_input = int(input('정수입력 : '))

print('원의 반지름 : ',num_input)
print('원의 둘래 : ',2*3.14*num_input)
print('원의 넓이 : ',3.14*num_input*num_input)
"""
"""#if로 예외 처리하기

num_input = input('정수입력 : ')
if num_input.isdigit():
    num_a = int(num_input)
    print('원의 반지름 : ',num_a)
    print('원의 둘래 : ',2*3.14*num_a)
    print('원의 넓이 : ',3.14*num_a*num_a)
else:
    print('정수를 입력하세요.')
"""

"""#try except 구문
try:
    num_input = input('정수입력 : ')
    num_input.isdigit()
    num_a = int(num_input)
    print('원의 반지름 : ',num_a)
    print('원의 둘래 : ',2*3.14*num_a)
    print('원의 넓이 : ',3.14*num_a*num_a)
except:
    print('정수를 입력하세요.')"""
"""
list_all = ['52','273','32','스파이','21']
list_num = []
for i in list_all:
    try:
        float(i)
        list_num.append(i)
    except:
        pass
print(list_num)"""
'''
list = ['52','273','32','스파이','21']
try:
    print(list[5])
except:
    print('존재하지 않는 인덱스 번호입니다.')

try:
#예외가 발생할 가능성이 있는 코드
except:
#예외가 발생했을 때 실행할 코드

else:
#예외가 발생하지 않았을떄 실행할 코드
'''
"""
try:
    num = int(input('정수를 입력하세요'))
except:
    print('정수를 입력하지 않았습니다.')
else:
    print('입력한 정수는',num,'입니다.')
finally:
    print('프로그램이 완전히 종료됩니다.')
#else는 다른 대부분의 언어에서는 없다.
#finally는 항상 실행된다.

#try + except
#try + except + else
#try + except + finally
#try + except + else + finally
#try +finally
"""
"""
def test():
    print('test()함수의 첫 줄입니다.')
    try:
        print('try 구문이 실행됬습니다.')
        return
        print('try 구문의 return 아래입니다.')
    except:
        print('except 구문이 실행됬습니다.')
    else:
        print('else 구문이 실행됬습니다.')
    finally:
        print('finally 구문이 실행됬습니다.')
    print('test()함수의 마지막줄입니다.')
print(test())
"""

print('프로그램 실행')
while True:
    try:
        print('try')
        break
        print('break')
    except:
        print('except')
    finally:
        print("finally")
    print('while')
print('프로그램 종료')

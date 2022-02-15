"""#001

fname = input('First Name : ')
print('Hello',fname)
print(f'Hello {fname}')

no1 = int(input('Plz enter your first number : '))
no2 = int(input('Plz enter your first number : '))

print(f'The total is {no1+no2}')
print(f'{no1}-{no2} is {no1-no2}')
"""
"""
days = int(input('Enter the number of days : '))
print(f'in {days}, days there are \n\t\t{days*24}hours\n\t\t{days*24*60}minutes\n\t\t{days*24*60*60}seconds')

"""
"""
l = input('Enter the number over 100 : ')
s = input('Enter the number over 10 : ')
# 사용자로부터 100이 넘는 숫자를 입력받고 10 미만의 숫자 하나를 입력받아
#작은숫자가 큰 숫자 안에 몇번 들어가는지 사용자 친화적으로 출력
print(f'{s} gose into {l} answer {l//s}times')
print(f'{s} gose into {l} answer {int(l/s)}times')
"""
"""
no1 = int(input('Enter first number : '))
no2 = int(input('Enter first number : '))
if no1 > no2 :
    print(no2,no1)
else:
    print(no1,no2)
"""
"""
#ask the user to enter a number between 10 and 20 If thay enter a number within this range,
#display the message 'Thank you' otherwise display the message 'incorrect number'
#10에서 20사이의 숫자입력을 요청한다. 만약 입력된 갑이 이 범위안의 숫자이면 'Thank you'아니면 'Incorrect number'를 입력

num = int(input('Enter a value between 10 and 20 : '))

if num >=10 and num<=20:
    print('Thank you')
else:
    print('Incorrect number')
"""
"""
#Ask the user to enter their favorite color. If thay enter 'red','RED' or 'Red'
#display the message ' I like red too',otherwise display the message 'I don`t like [Color], I prefer red.`

a = input('Enter the color : ')

if a in ['RED' , 'Red' , 'red']:
    print(f'I like {a} too')
else:
    print(f'I don`t like {a},I prefer red')
"""
"""
#Ask the user if it is raining and convert their answer to lower case
#so it doesnt matter what case they type it in. If they answer 'yes',ask if it is windy. If the answer 'yes' to this second question,
#display the answer 'It is too windy for an umbreally',otherwise dlsplay the message 'Take an umbrella'.
#If they did not answer yes to the first question, display the answer 'Enjoy your day'

weather = input('Is it rainning? : ')
#wind = input('Is it windy? : ')
weather = str.lower(weather)
if weather =='yes':
    wind  = input('Is it windy? :')
    wind = str.lower(wind)
    if wind == 'yes':
        print('It is too windy for an umbrella')
    else:
        print('Take an umbrella')
else:
    print('Enjoy your day')
"""

"""
if weather in ['Yes','yes','YES']:
    if wind in ['Yes','yes','YES']:
        print('It is too windy for an umbrella.')
    print('Take an umbrella')
else:
    print('Enjoy your day')
"""
"""
#ask the user`s age. if they are 18 or over, 'You cna drive'
# 17 , 'You can learn to drive'
# 16 , 'You can by a lottery ticket'
#16미만, 'You can go Trick or Treating'

age = int(input('What is your age? : '))

if age >= 18:
    print('You can vote')
elif age == 17:
    print('You cna learn to drive')
elif age == 16:
    print('You can by a lottery ticket')
else:
    print('You can go Trick or Treating')
"""
"""
#String

#ask yhe user to enter their name and then display the length of their name!

name = input('Enter your name : ')
print(len(name))
"""

"""
#Ask the user to enter their first name and lastname in lower case.
#Change the case to title case and join them together.
#Display the finished result.

fname = input('Enter your first name in lowercase : ')
lname = input('Enter your last name in lowercase : ')

fname = fname.title()
lname = lname.title()

name = fname + " " + lname
print(name)

"""
"""
#Ask the user to enter their first name. if the length of their first name is under five characters,
#ask them to enter their last name and join them together (without a space) and display the name in upper case.
#If the length of the first name is five or more characters, display their first name in lower case.
#display their first name in lower case.

fname = input('enter your first name : ')

if len(fname) < 5:
    lname = str(input('enter your last name : '))
    name = fname+lname
    print(name.upper())
#    print(f'{fname}{lname}')
else:
#    print(f'{fname}')
    print(fname.lower())
"""

# Pig Latin takes the first consonant of a word,
# moves it to the end of the word and adds on an ''ay'.
# if a word begins with a vowel you just add 'wy'to the end.

#For example, pig becomes igpay,banana becomes ananabay, and aadvark becomes aadvarkay.
#Create a rogram that wil ask the user to enter a word and  cahnge it nto Pig Latin.
#Make suer the new word is displayed in lower case.

n = input('what is word? : ')
first = n[0]
length = len(n)
rest = n[1:length]

if first in ['a','e','i','o','u']:
    newword = rest + first + 'ay'
else:
    newword = n + 'way'
print(newword.lower())


"""
n = input('what is word? : ')
if n in str(range(0,)):
    if range['a','e','i','o','u']:
        print(f'{range(1,0)}{range[0]}ay')
    else:
        print(f'{range}way')

"""

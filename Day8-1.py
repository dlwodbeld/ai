"""
클래스와 객체

C언어를 제외한 대부분의 언어는 객체지향 프로그래밍 언어이다. Object Oriented Programming : OOP 언어이다.


# 객체
students = [
    {'name':'슈가','korean':87,'math':98,'eng':88,'sci':95},
    {'name':'진','korean':90,'math':99,'eng':86,'sci':97},
    {'name':'카린','korean':99,'math':89,'eng':99,'sci':99}
]
print('이름','총점','평균',sep='\t\t')
for student in students:
    #학생들의 점수의 총합과 평균을 구하다.
    score_sum = student['korean'] + student['math'] + student['eng'] + student['sci']
    score_avg = score_sum / 4
    
    print(student['name'],score_sum,score_avg,sep='\t\t')

"""
 
"""
#딕셔너리로 학생 한명한명을 표현하고 이를 리스트로 묶어서 학생전체를 표현했다.
여러가지 속성을 가질 수 있는 대상을 '객체 object'라고 부른다.
그런데 딕셔너리로 객체를 하나하나 만들면 복잦ㅂ하고 귀찮다. 키를 모르면 사용하기도 어렵다.

함수 형태로 변형해보자.
 
 """"""
 # 딕셔너리로 리턴하는 함수
def create_student(name, korean, math, eng, sci):
  return {
      'name':name,
      'korean':korean,
      'math':math,
      'eng':eng,
      'sci':sci
  }

  # 학생들 리스트
students = [
            create_student('슈가', 87, 98, 88, 95),
            create_student('진', 90, 99, 86, 97),
            create_student('카린', 99, 89, 99, 99)
]

# 한명씩 반복
print('이름','총점','평균', sep='\t\t')
for student in students:
  # 학생들의 점수의 총합과 평균을 구하다
  score_sum = student['korean'] + student['math'] + student['eng'] + student['sci']
  score_avg = score_sum / 4

  print(student['name'], score_sum, score_avg, sep='\t\t')
# 딕셔너리로 리턴하는 함수
def create_student(name, korean, math, eng, sci):
  return {
      'name':name,
      'korean':korean,
      'math':math,
      'eng':eng,
      'sci':sci
  }

# 학생들의 점수를 처리하는 부분들도 함수로 만들자.

def student_get_sum(student):
  return student['korean'] + student['math'] + student['eng'] + student['sci']

def student_get_avg(student):
  return student_get_sum(student) / 4

def student_to_string(student):
  return '{}\t\t{}\t\t{}'.format(student['name'], student_get_sum(student), student_get_avg(student))

# 학생 리스트 선언

students = [
            create_student('슈가', 87, 98, 88, 95),
            create_student('진', 90, 99, 86, 97),
            create_student('카린', 99, 89, 99, 99)
]

print('이름','총점','평균', sep='\t\t')
for student in students:
  print(student_to_string(student))

#실행 결과가 이전과 같지만 코드가 분리되고있다. 학생이라는 객체와 관련된 기능이 위로 올라갔고
#이 객체들을 사용하는처리들은 아래로 내려갔다. 이렇게하면 '학생 객체와 관련된 기능'을 별도로 모듈로 빼서 관리할수도있다.

#객체와 관련된 코드를 분리할 수 있게 하는것이 객체 지향 프로그래밍의 핵심이다.
# 클래스라는 구조를 사용하면 위와 같은 형태의 코드를 좀더 쉽고 편하게 구현할 수있다.

print('이름','총점','평균',sep='\t\t')
for student in students:
    print(student_to_string(students))


#클래스선언
class Student:
    #생성자 constructor
    def __init__(self,name,kor,math,eng,sci):
        self.name = name
        self.kor = kor
        self.math = math
        self.eng = eng
        self.sci = sci

students = [
    student('슈가',87,98,88,95),
    student('진',90,99,86,97),
    student('카린',99,89,99,99)
]
student[0].name
student[1].name
student[1].math
"""

# method 매서드
# 클래스가 가지고 있는 함수를 매서드라고 부른다. 
# 매서드는 첫번째 매개변수로 self를 넣어야 한다. 
"""

class Student:
  # 생성자 constructor
  def __init__(self, name, korean, math, eng, sci):
    self.name = name
    self.korean = korean
    self.math = math
    self.eng  = eng 
    self.sci = sci

  def get_sum(self):
    return self.korean + self.math + self.eng + self.sci

  def get_avg(self):
    return self.get_sum() / 4

  def to_string(self):
    return '{}\t\t{}\t\t{}'.format(self.name, self.get_sum(), self.get_avg())


# 학생 리스트

students = [
            Student('슈가', 87, 98, 88, 95),
            Student('진', 90, 99, 86, 97),
            Student('카린', 99, 89, 99, 99)
]

print('이름','총점','평균', sep='\t\t')
for student in students:
  print(student.to_string())

  # 어떤 객체가 가지고 있는 어떤 함수(기능)를 명확하게 이해할수있으므로 편리하다.

"""

"""
result1 = 0
result2 = 0
# add함수는 입력받은 값을 이전에 계산한 값에 더한후 돌려주는 함수.
def add1(num):
    global result1
    result1 += num
    return result1
def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(5))
print(add2(2))
print(add2(4))
"""
"""
class Cal:
    #생성자
    def __init__(self):
        self.result = 0
    def add(self,num):
        self.result += num
        return self.result
    def sub(self,num):
        self.result -= num
        return self.result
    def add(self,num):
        self.result += num
        return self.result        

cal1 = Cal()
cal2 = Cal()

print(cal1.add(3))
print(cal1.add(4))
print(cal1.sub(2))
print(cal1.sub(3))


print(cal2.add(5))
print(cal2.add(6))
"""
"""
class FourCal:
    pass

a = FourCal()

print(type(a))
"""

"""

class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
a.setdata(4,2)

print(a.first)
print(a.second)
print(type(a))
b = FourCal()
b.setdata(1,3)


print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
"""

#생성자 constructor 객체가 생성될 떄 자동으로 호출되는 메서드를 의미한다.


class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
"""

a = FourCal(4,2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

"""

#상속 inheritance = 어떤 클래스를 만들떄 다른 클래스의 기능을 물려받아 사용한다.
"""
class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4,2)
print(a.add())
"""
"""
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4,2)
a.pow()

#매서드 오버라이딩 method overriding

a = FourCal(4,2)
print(a.div())

"""

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4.0)
a.div()


#클래스 변수
#객체변수는 다른 객체들에 영향받지 않고 독립적으로 그 값을 유지한다는점을 이미 알아보았다.
# 이번에는 객체변수와는 성격이 다른 클래스 변수에 대해 알아보자.

class Family:
    lastname = '김' #클래스 변수 선언.

Family.lastname

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)
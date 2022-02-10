# 클래스와 객체

# C언어를 제외한 대부분의 언어는 객체 지향 프로그래밍 Object Oriented Programming : OOP 언어이다. 
# 객체지향 언어는 클래스를 기반으로 객체를 만들고 그 객체들을 우선으로 생각해서 프로그래밍 하는것을 철학으로 한다. 

# 객체

students = [
            {'name':'슈가', 'korean':87, 'math':98, 'eng':88, 'sci':95},
            {'name':'진', 'korean':90, 'math':99, 'eng':86, 'sci':97},
            {'name':'카리', 'korean':99, 'math': 89, 'eng':99, 'sci':99}
]

print('이름','총점','평균', sep='\t\t')

for student in students:
  # 학생들의 점수의 총합과 평균을 구하다
  score_sum = student['korean'] + student['math'] + student['eng'] + student['sci']
  score_avg = score_sum / 4

  print(student['name'], score_sum, score_avg, sep='\t\t')

# 딕셔너리로 학생 한명한명을 표현하고 이를 리스트로 묶어서 학생 전체를 표현했다.  
# 여러가지 속성을 가질 수 있는 대상을 '객체'object 라고 부른다. 
# 그런데... 딕셔너리로 객체를 하나하나 만들면 복잡하고 귀찮다. 키를 모르면 사용하기도 어렵다. 

# 함수형태로 변형해보자.
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
            create_student('카리', 99, 89, 99, 99)
]

# 한명씩 반복
print('이름','총점','평균', sep='\t\t')
for student in students:
  # 학생들의 점수의 총합과 평균을 구하다
  score_sum = student['korean'] + student['math'] + student['eng'] + student['sci']
  score_avg = score_sum / 4
  
  print(student['name'], score_sum, score_avg, sep='\t\t')
  # 실행 결과는 이전과 동일하다. 그럼 조금 더 변형해보자 .
# 현재 총점과 평균을 구하는 처리는 학생을 대상으로만 이루어진다. 따라서 학생을 매개변수로 받는 형태의 함수로
# 만들면 코드가 좀 더 균형잡히게 된다. 


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
            create_student('카리', 99, 89, 99, 99)
]

print('이름','총점','평균', sep='\t\t')
for student in students:
  print(student_to_string(student))


  # 실행 결과가 이전과 같지만 코드가 분리되고 있다. 학생이라는 객체와 관련된 기능이 위로 올라갔고
  # 이 객체들을 사용하는 처리들은 아래로 내려갔다. 이렇게 하면 '학생 객체와 관련된 기능'를
  # 별도의 모듈로 빼서 관리할수도 있다. 

  # 객체와 관련된 코드를 분리할수 있게 하는 것이 객체 지향 프로그래밍의 핵심이다. 
  # 클래스라는 구조를 사용하면 위와 같은 형태의 코드를 좀 더 쉽고 편하게 구현할 수 있다. 
  # 클래스 선언
class Student:
  # 생성자 constructor
  def __init__(self, name, korean, math, eng, sci):
    self.name = name
    self.korean = korean
    self.math = math
    self.eng  = eng 
    self.sci = sci

# 학생 리스트

students = [
            Student('슈가', 87, 98, 88, 95),
            Student('진', 90, 99, 86, 97),
            Student('카리', 99, 89, 99, 99)
]
students[0].name
students[1].name
students[1].math
# method 매서드
# 클래스가 가지고 있는 함수를 매서드라고 부른다. 
# 매서드는 첫번째 매개변수로 self를 넣어야 한다. 


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
            Student('카리', 99, 89, 99, 99)
]

print('이름','총점','평균', sep='\t\t')
for student in students:
  print(student.to_string())

  # 어떤 객체가 가지고 있는 어떤 함수(기능)를 명확하게 이해할 수 있으므로 매우 편리하다. 
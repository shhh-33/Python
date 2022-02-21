# -*- coding: utf-8 -*-
"""파이썬 - 소개~반복문 실습.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/ehpub/81f56b5bde0ca196c1b0ce563dc27434/.ipynb

1. 사용자로부터 삼각형의 밑변과 높이를 입력받아 넓이를 출력하시오.
   밑변과 높이는 실수를 입력할 수 있으며 넓이는 소수점 이하 2째 자리까지 출력하시오.
"""

bottom = float(input("밑변:"))
height = float(input("높이:"))
print(f"넓이:{(bottom*height/2):.2f}")

"""2. 두 개의 정수를 입력받아 작은 수가 큰 수의 약수인지 아닌지를 출력하시오."""

num1 = int(input("첫 번째 정수:"))
num2 = int(input("두 번째 정수:"))
if num1 > num2:
  num1,num2 = num2,num1
if num2 % num1 == 0:
  print("약수")
else:
  print("No 약수")

"""3. 두 개의 정수를 입력받아 두 개의 정수 사이의 정수의 합계를 구하여 출력하시오.

"""

num1 = int(input("첫 번째 정수:"))
num2 = int(input("두 번째 정수:"))
if num1 > num2:
  num1,num2 = num2,num1
s = 0
for i in range(num1,num2+1):
  s += i
print(f"{num1}~{num2} 합계:{s}")

"""4. n개의 정수를 입력받아 평균과 표준 편차를 구하시오.

"""

import math
n = int(input("입력할 개수:"))
nums=[]
for i in range(n):
  num = int(input(f"{i+1}번째 정수:"))
  nums.append(num)
avg = sum(nums)/n
print(f"평균:{avg}")

ss=0
for elem in nums:
  ss += (avg - elem)**2
var = ss/n #분산
stddev = math.sqrt(var) #표준편차
print(f"표준 편차:{stddev:.2f}")

"""5. n명의 국어, 영어, 수학 점수를 입력받아 출력하시오.

"""

subjects = ("국어","영어","수학")
n = int(input("입력할 학생 수:"))
m_dict=dict()
for i in range(n):
  name = input(f"{i+1}번째 학생 이름:")
  scores =[]
  for subject in subjects:
    score = int(input(f"{subject} 점수:"))
    scores.append(score)
  m_dict[name] = scores
print(m_dict)

"""6. n명의 국어, 영어, 수학 점수를 입력받아 과목별 합계, 평균, 표준 편차를 출력하시오."""

import math
subjects = ("국어","영어","수학")
n = int(input("입력할 학생 수:"))

scores=[]
scores.append([])#국어
scores.append([])#영어
scores.append([])#수학

for i in range(n):
  for si, subject in enumerate(subjects):
    score = int(input(f"{subject} 점수:"))
    scores[si].append(score)

print("\n\n=========================")
for si , subject in enumerate(subjects):
  avg = sum(scores[si])/len(scores[si])
  print(f"{subjects[si]} 평균: {avg:.2f}")  
  ss=0
  for score in scores[si]:
    ss += (avg - score)**2
  var = ss/n #분산
  stddev = math.sqrt(var) #표준편차
  print(f"{subjects[si]} 표준편차: {stddev:.2f}")
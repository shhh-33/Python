# -*- coding: utf-8 -*-
"""파이썬 - 반복문(while).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V5IQnQeO5ufdw4qnKAE5ZfNnUiZ1cPIZ

# while 반복문

특정 조건이 참일 때 반복
"""

#사용자로부터 정수를 입력받아 합계를 계산하여 출력하시오.
#사용자가 음수를 입력하면 더 이상 입력받지 않는다.

sum = 0#합계:=0
number = 0
while number>=0:#반복 number가 음수가 아니라면
  sum += number#합계:= 합계 + number
  number = int(input("정수:"))
print(sum)#합계 출력

sum = 0#합계:=0
while True:#무한 루프
  number = int(input("정수:"))
  if number < 0:
    break #반복문(루프) 탈출
  sum += number#합계:= 합계 + number  
print(sum)#합계 출력

for i in range(10):
  print(i,end=' ')

i = 0
while i<10:
  print(i,end=' ')
  i+=1

i=0
while i<100:  
  i+=1
  if i %2 == 0:
    print(i,end=' ')
  elif i % 3==0:
    continue
  else:
    print(f'.{i}.')
# -*- coding: utf-8 -*-
"""통계분석시각화-Numpy 소개.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CpMlifXDGThzHq5nZtUvMj6a2SWnhrF0

# Numpy 소개
"""

import numpy as np

"""numpy는 선형 시퀀스를 배열 개체로 취급"""

ls = [1,2,3]
arr = np.array(ls)
print(arr)

arr = np.array([1,2,3])
print(arr)

print("구조:",arr.shape)
print("차원:",arr.ndim)

"""다차원 배열"""

ls = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
arr = np.array(ls)
print(arr)

print("구조:",arr.shape)
print("차원:",arr.ndim)

"""# 다양한 방법의 생성"""

z_arr = np.zeros(10)
print(z_arr)
print("구조:",z_arr.shape)
print("차원:",z_arr.ndim)
print("원소 형식:",z_arr.dtype)

z_arr = np.zeros(10,dtype=int)
print(z_arr)
print("구조:",z_arr.shape)
print("차원:",z_arr.ndim)
print("원소 형식:",z_arr.dtype)

z_arr = np.zeros((2,3))
print(z_arr)
print("구조:",z_arr.shape)
print("차원:",z_arr.ndim)
print("원소 형식:",z_arr.dtype)

def view_arr_info(arr):
  print(arr)
  print("구조:",arr.shape)
  print("차원:",arr.ndim)
  print("원소 형식:",arr.dtype)

z_arr = np.zeros((3,2,4),dtype=int)
view_arr_info(z_arr)

o_arr = np.ones(10)
view_arr_info(o_arr)

s_arr = np.arange(100)
view_arr_info(s_arr)

s_arr = np.arange(50,100)
view_arr_info(s_arr)

r_arr = np.random.randint(0,100,size=10,dtype=int)
view_arr_info(r_arr)

"""# 기본적인 사용"""

a1 = np.arange(1,100)
view_arr_info(a1)

print(a1[4]) #인덱스를 통해 원소에 접근
a1[4]=9
print(a1[4])

print(a1[2:8]) #슬라이스를 통해 부분 원소를 선택
print(a1[:8])
print(a1[8:])

a1 = np.arange(0,100)
view_arr_info(a1)
a2 = a1.reshape(5,20)
view_arr_info(a2)

print(a2[0])#인덱스 0인 원소: 리스트[0,1,2,...,19]
print(a2[0][2])#인덱스 0인 원소: 리스트[0,1,2,...,19]의 인덱스 2인 원소

#음의 정수로 인덱스를 표현하면 뒤에서 부터 접근(-1부터 시작)
print(a2[0][-1])#인덱스 0인 원소: 리스트[0,1,2,...,19]의 인덱스 -1인 원소

"""# 구조 변경"""

a1 = np.arange(100)
view_arr_info(a1)

a2 = a1.reshape((20,-1))
view_arr_info(a2)

a1 = np.arange(784)
view_arr_info(a1)

a2 = a1.reshape(28,-1)
view_arr_info(a2)

"""# 쉬어가는 코너"""

from tensorflow import keras

data = keras.datasets.mnist.load_data() #손글씨 데이터를 다운로드

train_data, test_data = data #학습용 데이터, 평가용 데이터로 분리
image_train, label_train = train_data #이미지, 실제값

print(image_train.shape)
print(label_train.shape)

for r in range(28):
  for c in range(28):
    if(image_train[0][r][c] == 0):
      print("  ",end='')
    else:
      print("■",end='')
  print()
print(label_train[0])
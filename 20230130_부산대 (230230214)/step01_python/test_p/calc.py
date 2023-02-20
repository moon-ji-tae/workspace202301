#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# test_p 폴더안의 calc.py 

# 사칙연산 함수 정의 
def calc_print(x,y):
    print(f'{x} + {y} = {x+y}')
    print(f'{x} - {y} = {x-y}')
    print(f'{x} * {y} = {x*y}')
    print(f'{x} / {y} = {(x/y):.2f}')    

# 테스트 함수 정의 
def info():
    print('test_p 폴더안의 calc.py 호출')


# gugu.py 
# n 단 출력 함수 정의 
def gugu_print1():
    data = int(input('출력할 단의 숫자를 입력하세요?...'))
    for i in range(1,10):
        print(f'{data} X {i} = {data*i}')

# 전체 구구단 출력 함수 정의 
def gugu_print2():
    for i in range(2,10):
        for j in range(1,10):
            print(f'{i} X {j} = {i*j}')
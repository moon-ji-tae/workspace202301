def calc_plus(a,b):
    if type(a) == int and type(b):
        print(f'{a}+{b}={a+b}')
    else:
        print('연산을 할 수 없습니다')

def calc_minus(a,b):
    if type(a)== int and type(b):
        print(f'{a}-{b}={a-b}')
    else:
        print('연산을 할 수 없습니다')

def calc_multy(a, b):
    if type(a)== int and type(b):
        print(f'{a}*{b}={a*b}')
    else:
        print('연산을 할 수 없습니다')

def calc_divide(a, b):
    if type(a)== int and type(b):
        print(f'{a}/{b}={a/b}')
    else:
        print('연산을 할 수 없습니다')

def info():
    print('test_p 폴도안의 calc.py 호출')
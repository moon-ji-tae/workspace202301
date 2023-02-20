import random
def make_lotto3():     
    num_list = list(range(1,47))    
    lotto_list = random.sample(num_list, 6)    
    return print(f'추천 로또 번호 {sorted(lotto_list)}')
print(make_lotto3())
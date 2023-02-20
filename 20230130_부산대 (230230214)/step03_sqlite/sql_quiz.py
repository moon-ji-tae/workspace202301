#!/usr/bin/env python
# coding: utf-8

# In[65]:


import  sqlite3

conn = sqlite3.connect("address.db")
cursor = conn.cursor()
sql =   ''' create table if not exists addr (
                id integer not null primary key autoincrement,
                name text not null,
                mobile text,
                email text,
                address text);
        '''
cursor.execute(sql)


# In[66]:



#
def menu():
    print('=' * 20)
    print('주소록 메뉴')
    print('=' * 20)
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 수정')
    print('4. 연락처 삭제')
    print('5. 연락처 초기화')
    print('6. 종료')
    print('='*20)
    action = int(input('메뉴 선택 :'  ))
    return action


# In[67]:


def insert_record():
    print('='* 20)
    name = input('이름: ')
    phone = input('핸드폰 : ')
    email = input('이메일: ')
    address = input('주소 : ') 
    
    sql =   ''' insert into addr (name, mobile, email, address) 
                        values (?,    ?,      ?,     ?);               
            ''' 
    cursor.execute(sql, (name, phone, email, address))
    conn.commit()


# In[68]:


# 레코드 수정 함수 
def update_record():
    print()
    print('='*70)
    print('레코드 수정')
    print('='*70)
    id = input('레코드 수정 아이디 ...')
    menu = input('수정할 컬럼의 번호 입력 (1.이름 2.핸드폰 3.이메일 4.주소) >> ')
    if menu == '1':
        name = input('이름 >> ')
        sql = " update addr set name=? where id=?; "
        cursor.execute(sql, (name, id))
    elif menu == '2':
        mobile = input('핸드폰 >> ')
        sql = " update addr set mobile=? where id=?; "
        cursor.execute(sql, (mobile, id))
    elif menu == '3':
        email = input('이메일 >> ') 
        sql = " update addr set email=? where id=?; "
        cursor.execute(sql, (email, id))           
    elif menu == '4':
        address = input('주소 >> ')    
        sql = " update addr set address=? where id=?; "
        cursor.execute(sql, (address, id))            
    else:
        print('입력 오류')
        
    conn.commit()


# In[69]:


# 레코드 출력함수 
def print_record():
    print()
    print('='*70)
    print('  번호       이름        핸드폰            이메일             주소')
    print('='*70)
    # 전체 레코드 조회 후 파이썬의 데이타로 저장( 리스트안의 튜플)
    cursor.execute("select * from addr;")
    data_list = cursor.fetchall()
    for id, name, mobile, email, address in data_list:
        print(f'{id:>5} {name:>10} {mobile:>15} {email:>20} {address}')


# In[70]:


# 레코드 삭제 함수 
def delete_record():
    print()
    print('='*70)
    print('레코드 삭제')
    print('='*70)
    id = input('레코드 삭제 아이디 ...')    
    sql = " delete from addr where id=?; "
    cursor.execute(sql, (id,))
    conn.commit()
    print('레코드 삭제 완료')
    


# In[71]:


# 레코드 전체 삭제함수 
def delete_all_record():
    print()
    sql = " delete from addr; "
    cursor.execute(sql)
    conn.commit()
    print('레코드 모두 삭제 완료')


# In[72]:


while True:
    action = menu() 
    if action ==1 :
        insert_record()
    elif action ==2:
        print_record()
    elif action == 3:
        update_record()
    elif action == 4:
        delete_record()
    elif action == 5:
        delete_all_record()
    elif action == 6:
        print('종료합니다')
        break
    else:
        print('선택 오류')
    

conn.commit()


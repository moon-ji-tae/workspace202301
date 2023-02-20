# 1) 관련 모듈 임포트 
import sqlite3

# 2) 데이타베이스 연결 - 경로에 없으면 새로 생성. 있으면 연결 
# 연결변수명 = sqlite3.connect(데이타베이스파일경로)
conn = sqlite3.connect("book.db")
# sql실행객체 생성
# 커서변수명 = 연결변수명.
cursor = conn.cursor()
print(type(cursor))

# 3) 테이블 생성 
# 커서변수명.execute(SQL명령)
# 아이디, 책제목, 저자, 페이지수, 가격 => book1 테이블 
cursor.execute(''' 
               create table if not exists book1 (
                   id integer not null primary key autoincrement,
                   title text not null,
                   writer text,
                   page integer,
                   price integer
               );
''')

# 4) 레코드 추가 1 
# cursor.execute(''' 
#                  insert into book1 (title, writer, page, price)
#                     values ('파이썬완전정복', '김파이', 200, 45000);   
# ''')

# 5) 레코드 추가 2 
# 커서변수.executemany(sql명령변수, 데이타리스트)
# sql 명령 변수 설정. 실제데이타값은 ? 로 처리 
sql = '''
        insert into book1 (title, writer, page, price)
                    values (?, ?, ?, ?);
'''
# 데이타리스트 - 2차원 
data_list = [ ('슬램덩크1', '이노우에 다케히코', 200, 15000),
              ('슬램덩크2', '이노우에 다케히코', 200, 15000),
              ('슬램덩크3', '이노우에 다케히코', 200, 15000) ]
# 명령 실행 
cursor.executemany(sql, data_list)



# 데이타베이스 반영 
conn.commit()

# 데이타베이스 종료 
# 자원반납 = 마지막 명령어로 사용 
conn.close()
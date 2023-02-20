# 레코드 조회 
# cursor.execute(sql select명령)
# 저장변수 = cursor.fetchall() / fetchone() / fetchmany(숫자)

# 1) 관련 모듈 임포트 
import sqlite3

# 2) 데이타베이스 연결 - 경로에 없으면 새로 생성. 있으면 연결 
# 연결변수명 = sqlite3.connect(데이타베이스파일경로)
conn = sqlite3.connect("test.db")
# sql실행객체 생성
# 커서변수명 = 연결변수명.
cursor = conn.cursor()

# 3) 테이블에서 하나의 레코드만 저장 
# sql 명령실행
cursor.execute("select * from albums;")
# 파이썬 데이타로 저장 <= 첫번째 레코드, 튜플 
result = cursor.fetchone()
print(type(result))
print(result)
print('='*30)
print('='*30)

# 4) 테이블에서 여러개의 레코드 저장 
# sql 명령실행
cursor.execute("select * from albums limit 10;")
# 파이썬 데이타로 저장 <= 2차원형태 리스트안의 튜플  
result2 = cursor.fetchall()
print('='*30)
print(type(result2))
print(result2[0])
print('='*30)
for record in result2:
    print(record)
print('='*30)
for id, title, a_id  in result2:
    print(f"{id} / {title} / {a_id}")
    
    


# 데이타베이스 종료 
# 자원반납 = 마지막 명령어로 사용 
conn.close()
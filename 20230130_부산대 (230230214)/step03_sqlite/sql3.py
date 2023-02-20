# 1) 관련 모듈 임포트 
import sqlite3

# 2) 데이타베이스 연결 - 경로에 없으면 새로 생성. 있으면 연결 
# 연결변수명 = sqlite3.connect(데이타베이스파일경로)
conn = sqlite3.connect("book.db")
# sql실행객체 생성
# 커서변수명 = 연결변수명.
cursor = conn.cursor()

# 3) 레코드 수정 1
cursor.execute(" update book1 set price=0 where id=2; ")

# 4) 레코드 수정 2
# 실제 교체값을 ?로 지정 
sql = " update book1 set price=? where id=?; "
# execute(sql명령변수, 실제데이타튜플)
cursor.execute(sql, (30, 3))

# 5) 레코드 삭제
# 실제 교체값을 ?로 지정 
sql = " delete from book1 where id=?; "
# execute(sql명령변수, 실제데이타튜플)
cursor.execute(sql, (1,))



# 데이타베이스 반영 
conn.commit()

# 데이타베이스 종료 
# 자원반납 = 마지막 명령어로 사용 
conn.close()


-- 테이블 생성 
-- id : pk, 자동숫자, 정수형 
-- name : 문자열 
-- age : 나이, 정수형 
-- addr : 주소, 문자열, 서울 값을 초기값 
-- CREATE  TABLE student (
-- 	id INTEGER PRIMARY key AUTOINCREMENT NOT NULL,
-- 	name TEXT NOT NULL,
-- 	age INTEGER NOT NULL,
-- 	addr TEXT DEFAULT "서울" NOT NULL

-- 레코드 삽입 
-- INSERT INTO 테이블명 (컬럼명1, 컬럼명2 ...) VALUES (값1, 값2 ....);
/*
INSERT INTO student  (name, age, addr) VALUES ('홍길동', 25, '부산');
INSERT INTO student  (name, age) VALUES ('이순신', 35);
INSERT INTO student  (name, age, addr) VALUES ('마동탁', 40, '대구');
*/

-- 레코드 삭제
-- DELETE FROM 테이블명 WHERE 절;
-- DELETE FROM student WHERE id=2;


-- 레코드 수정
-- UPDATE 테이블명 SET 컬럼명1=값1, 컬럼명2=값2 ...  WHERE 절;
-- UPDATE student SET age = 30  WHERE name='홍길동';
-- UPDATE student SET addr='울산',  age=33  WHERE id=3;
-- SELECT * FROM student;

-- 기존 테이블 이용해서 새 테이블 생성 
-- CREATE TABLE 테이블명 AS SELECT 절 
-- student 테이블 복사해서 student_a 테이블 생성 
/*
CREATE TABLE student_a 
	AS SELECT * FROM  student;
SELECT * FROM student_a;
*/
-- student 테이블에서 id, name 컬럼만 복사해서 student_b 테이블 생성 
CREATE TABLE student_b 
	AS SELECT id, name FROM  student;
SELECT * FROM student_b;





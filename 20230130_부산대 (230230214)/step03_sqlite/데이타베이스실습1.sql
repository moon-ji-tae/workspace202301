/*
   select * 또는 필드명 from 테이블명 
                 where 절 limit 숫자;
*/
-- employees 테이블의 모든 레코드 보기
-- SELECT * FROM employees;

-- employees 테이블에서 LastName, FirstName 컬럼만 출력
-- SELECT LastName, FirstName FROM employees;

-- employees 테이블에서 3명의 정보만 출력 
-- SELECT * FROM employees LIMIT 3;

-- employees 테이블에서 3명의 아이디와 주소 정보만 출력 
-- SELECT EmployeeId, Address 
-- 		FROM employees LIMIT 3;


-- customers 테이블에서 아이디값이 10인 레코드 출력 
-- SELECT * from customers
-- 	WHERE CustomerId = 10;

-- customers 테이블에서 아이디값이 10~30 인 레코드 출력 
-- SELECT * from customers
-- 	WHERE CustomerId >= 10 and CustomerId <= 30;

-- customers 테이블에서 국적(Country)이 Canada인 레코드 출력 
SELECT * from customers
	WHERE Country = 'Canada';

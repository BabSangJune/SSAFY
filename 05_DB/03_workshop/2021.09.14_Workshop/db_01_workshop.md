# SQL & ORM

### Background

> - SQL
> - Database

### Goal

> - 테이블의 생성
> - 데이터의 생성 및 조회
> - SQL과 ORM 비교

### Problem

> ##### Table Name : countries
> | name      | data type |
> | --------- | --------- |
> | room_num  | text      |
> | check_in  | text      |
> | check_out | text      |
> | grade     | text      |
> | price     | integer   |
>
> | id   | room_num | check_in   | check_out  | grade    | price |
> | ---- | -------- | ---------- | ---------- | -------- | ----- |
> | 1    | B203     | 2019-12-31 | 2020-01-03 | suite    | 900   |
> | 2    | 1102     | 2020-01-04 | 2020-01-08 | suite    | 850   |
> | 3    | 303      | 2020-01-01 | 2020-01-03 | deluxe   | 500   |
> | 4    | 807      | 2020-01-04 | 2020-01-07 | superior | 300   |

<br>

#### 1. SQL Query

> 위 counries 테이블을 바탕으로 아래 문제에 해당하는 SQL query문을 작성하고 실행하시오.

###### 1-1. countries 테이블을 생성하시오.

###### 1-2. 데이터를 입력하시오.

###### 1-3. 테이블의 이름을 hotels로 변경하시오.

###### 1-4. 객실 가격을 내림차순으로 정렬하여 상위 2개의 room_num과 price를 조회하시오.

###### 1-5. grade 별로 분류하고 분류된 grade 개수를 내림차순으로 조회하시오.

###### 1-6. 객실의 위치가 지하 혹은 등급이 deluxe인 객실의 모든 정보를 조회하시오.

###### 1-7. 지상층 객실이면서 2020년 1월 4일에 체크인 한 객실의 목록을 price 오름차순으로 조회하시오.

(답)

```sql
-- 1-1
CREATE TABLE countries (
id INTEGER PRIMARY KEY,
room_num TEXT,
check_in TEXT,
check_out TEXT,
grade TEXT,
price INTEGER
);

-- 1-2
INSERT INTO countries VALUES 
(1, 'B203', '2019-12-31', '2020-01-03', 'suite', 900),
(2, '1102','2020-01-04', '2020-01-08', 'suite', 850),
(3, '303','2020-01-01', '2020-01-03', 'deluxe', 500),
(4, '807','2020-01-04', '2020-01-07', 'superior', 300);

-- 1-3
ALTER TABLE countries RENAME TO hotels;

-- 1-4
SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2;

-- 1-5
SELECT grade, COUNT(*) FROM hotels GROUP BY grade ORDER BY COUNT(*) DESC;

-- 1-6
SELECT * FROM hotels WHERE room_num LIKE 'B%' OR grade == 'deluxe';

-- 1-7
SELECT room_num FROM hotels WHERE room_num NOT LIKE 'B%' and check_in == '2020-01-04' ORDER BY price;
```

<br>

#### 2. SQL ORM 비교하기

> 주어진 정보를 활용하여 작성된 SQL문과 대응하는 ORM문을 작성하고 실행하시오.
>
> ##### Table Name : users
>
> | name       | data type   |
> | ---------- | ----------- |
> | id         | integer(pk) |
> | first_name | text        |
> | last_name  | text        |
> | age        | integer     |
> | country    | text        |
> | phone      | text        |
> | balance    | integer     |

###### 2-1 user 테이블 전체 데이터를 조회하시오. 

```sql
SELECT * FROM users_user;
```
```python
# 2-1
User.objects.all()
```

=> (1, 정호, 유,  40, 전라북도, 016-7280-2855,370), (2, 경희, 이, 36, 경상남도, 011-9854-5311, 5900), ...
<br>

###### 2-2 id가 19인 사림의 age를 조회하시오. 

```sql
SELECT age FROM users_user WHERE id = 19;
```
```python
# 2-2
User.objects.get(pk=19)
```

=> 26
<br>

###### 2-3 모든 사람의 age를 조회하시오. 

```sql
SELECT age FROM users_user;
```
```python
# 2-3
User.objects.all().values('age')
```
=> 40, 36, 37, 40, ...
<br>

###### 2-4 age가 40 이하인 사림들의 id와 balance를 조회하시오. 

```sql
SELECT id, balance FROM users_user WHERE age <= 40;
```
```python
# 2-4
User.objects.filter(age__lte=40).values('pk','balance')
```
=> (1, 370), (2, 5900), (3, 3100), (4, 250000), ...
<br>

###### 2-5 last_name이 ‘김’이고 balance가 500 이상인 사람들의 first_name을 조회하시오.

```sql
SELECT first_name FROM users_user
WHERE last_name = '김' AND balance >= 500;
```
```python
# 2-5
User.objects.filter(last_name='김', balance__gte=500).values('first_name')
```

=> 예진, 서현, 서영, 영일, ...
<br>

###### 2-6 first_name이 ‘수’로 끝나면서 행정구역이 경기도인 사람들의 balance를 조회하시오. 

```sql
SELECT balance FROM users_user
WHERE first_name LIKE '%수' AND country = '경기도';
```
```python
# 2-6
User.objects.filter(first_name__endswith='수', country='경기도').values('balance')
```

=> 500, 370
<br>

###### 2-7 balance가 2000 이상이거나 age가 40 이하인 사람의 총 인원수를 구하시오. 

```sql
SELECT COUNT(*) FROM users_user
WHERE balance >= 2000 or age <= 40;
```
```python
# 2-7
from django.db.models import Q
User.objects.filter(Q(balance__gte=2000)|Q(age__lte=40)).count()
```

=> 99
<br>

###### 2-8 phone 앞자리가 ‘010’으로 시작하는 사람의 총원을 구하시오. 

```sql
SELECT COUNT(*) FROM users_user
WHERE phone LIKE '010%';
```
```python
# 2-8
User.objects.filter(phone__startswith='010').count()
```

=> 21
<br>

###### 2-9 이름이 ‘김옥자’인 사람의 행정구역을 경기도로 수정하시오. 
```sql
UPDATE users_user SET country = '경기도'
WHERE first_name = '옥자' AND last_name = '김';

UPDATE country FROM users_user
WHERE first_name = '옥자' AND last_name = '김';
```
```python
# 2-9
user = User.objects.filter(first_name='옥자', last_name='김')
user.country = '경기도'
user.save()
```

<br>

###### 2-10 이름이 ‘백진호’인 사람을 삭제하시오. 

```sql
DELETE FROM users_user
WHERE first_name = '진호' AND last_name ='백';

SELECT * FROM users_user
WHERE first_name = '진호' AND last_name ='백';
```
```python
# 2-10
User.objects.filter(first_name='진호', last_name='백').delete()
```

<br>

###### 2-11 balance를 기준으로 상위 4명의 first_name, last_name, balance를 조회하시오. 

```sql
SELECT first_name, last_name, balance FROM users_user
ORDER BY balance DESC LIMIT 4;
```
```python
# 2-11
User.objects.order_by('-balance')[:4].values('first_name', 'last_name', 'balance')
```

=> (순옥, 김, 1000000), (은주, 김, 950000), (미경, 이, 890000), (동현, 이, 790000)
<br>

###### 2-12 phone에 ‘123’을 포함하고 age가 30미만인 정보를 조회하시오. 

```sql
SELECT * FROM users_user
WHERE phone LIKE '%123%' AND age < 30;
```
```python
# 2-12
User.objects.filter(phone__contains='123',age__lt=30)
```

=> (93, 하은, 손, 18, 전라남도, 02-9618-1232, 4800)
<br>

###### 2-13 phone이 ‘010’으로 시작하는 사람들의 행정 구역을 중복 없이 조회하시오. 

```sql
SELECT DISTINCT country FROM users_user
WHERE phone LIKE '010%';
```
```python
# 2-13
User.objects.filter(phone__startswith='010').values('country').distinct()
```

=> 충청북도, 경상북도, 경기도, 제주특별자치도, 경상남도, 전라남도, 강원도, 전라북도
<br>

###### 2-14 모든 인원의 평균 age를 구하시오. 

```sql
SELECT AVG(age) FROM users_user;
```
```python
# 2-14
from django.db.models import Avg
User.objects.all().aggregate(Avg('age'))
```

=> 28.3434343434343
<br>

###### 2-15 박씨의 평균 balance를 구하시오. 

```sql
SELECT AVG(balance) FROM users_user
WHERE last_name = '박';
```
```python
# 2-15
from django.db.models import Avg
User.objects.filter(last_name='박').aggregate(Avg('balance'))
```

=> 196114.2857142857
<br>

###### 2-16 경상북도에 사는 사람 중 가장 많은 balance의 액수를 구하시오. 

```sql
SELECT MAX(balance) FROM users_user
WHERE country = '경상북도';
```
```python
# 2-16
from django.db.models import Max
User.objects.filter(country='경상북도').aggregate(Max('balance'))
```

=> 400000
<br>

###### 2-17 제주특별자치도에 사는 사람 중 balance가 가장 많은 사람의 first_name을 구하시오.

```sql
SELECT first_name FROM users_user
WHERE country = '제주특별자치도' ORDER BY balance DESC LIMIT 1;
```
```python
# 2-17
User.objects.filter(country='제주특별자치도').order_by('-balance')[:1].values('first_name')
```

=> 순옥
<br>
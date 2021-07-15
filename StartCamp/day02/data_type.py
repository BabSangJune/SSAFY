# 숫자
number1 = 3      #정수
number2 = 3.14   #실수
number3 = 3 + 4j #복소수

print(type(number1))
print(type(number2))
print(type(number3))

# 문자
string1 = '문자열'
string2 = "문자열"
print(type(string1))
print(type(string2))

# 참/거짓 (boolean)
# 참/거짓 (Boolean)
boolean1 = True
boolean2 = False
print(type(boolean1))
print(type(boolean2))

# 형변환
num1 = 3
num2 = 4.5

# 1. 묵시적 형변환 (자동 형변환)
result1 = num1 + num2
print(result1, type(result1))
# 2. 명시적 형변환
result2 = num1 + int(num2)
print(result2, type(result2))


#실수의 연산을 할때는 항상 주의하자.
#이거 실행 안됨. 
if 0.1 + 0.1 + 0.1 == 0.3:
    print("이거 실행되나?")



#문자열 숫자

string_number = "6"
# print(string_number + 5)
print(int(string_number) + 5)
print(string_number + str(5))

#f-string  python 3.6v 이상에서만 사용가능
# print("황보창님 안녕하세요.!")
# print("홍지범님 안녕하세요.!")
# print("박신영님 안녕하세요.!")
# print("박수아님 안녕하세요.!")

name = "황보창"
money = 1000
hello = f'{name}님 축하드립니다. {money}만원 당첨!'

print(hello)

names = ['황보창', '홍지범', '박신영', '박수아']
for n in names:
    print(f'{n}님 반갑습니다.')


# 리스트 사용법

print(names[3])
names.append('강동욱')
print(names[4])
names[4] = '강동옥'
print(names[4])

#가장 마지막 원소를 가지고 오고 싶다.... 
print(names[len(names)-1])
print(names[-1])

#  0  1  2  3  4
# -5 -4 -3 -2 -1  단 이 방법은 권장하지 않음.

# 실습
# 1.어제 먹은 음식들로 채워진 리스트를 만들어보시오. (적어도 3개 이상)
# 2.첫번째 음식을 출력하시오.
# 3.두번째 음식을 초밥으로 바꾸시오...

food = ['쌀', '김치', '오이', '닭가슴살', '야채']

print(food[0])
food[1] = '초밥'
print(food[1])
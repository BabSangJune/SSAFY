"""
연습장
"""

'''
#딕셔너리 반복문 돌리자
st = {'양':99, '명':97, '균':68}

#오류가 낟나.
for key, value in st:
    print(key, value)
# 에러메시지
# for key, value in st:
# ValueError: not enough values to unpack (expected 2, got 1)

#키를 기본으로 가져옴
for key in st:
    print(key)
    print(st[key])

for key in st.keys():
    print(key)

#value만 가져옴.
for value in st.values():
    print(value)

# key  , value를 동시에 가지고 오고 싶다.
for key, value in st.items():
    print(key, value)
'''


# def example1(*args):
#     print(type(args))

# def example2(**kwargs):
#     print(type(kwargs))
#     kwargs.keys()
#     kwargs.values()
#     kwargs.item()
#     print(list(kwargs))

#     for key in kwargs.items():
#         print(f'{key} 키 / {value} 벨류')



# # print(example1())
# print(example2(a = 1, b = 2, c = 2))

#함수 호출 코드의 args 순서 => 1. positional > 2. keyword

# def example3(a, b, *args, **kwargs):
#     print('a', a)
#     print('b', b)
#     print('args', args)
#     print('kwargs', kwargs)
#
# print(example3(1, 2, 1, 3, 4, c=2)) #b=2들어가면 에러뜸 인자에 b가 있어서
# # a, b, *args
# # a, b **args
# # *args, **kwargs


# def snail(height, day, night):
#     one_day = day - night #하루 움직이는 거리
#     cnt = height // one_day
#     arrive = 0

#     for i in range(1, cnt+1):
#         if cnt - one_day * i == 0:
#             arrive = height // one_day

#     return arrive

    
# print(snail(100, 5, 2))


# def snail(height, day, night):
#     arrive = height // (day - night)
#     return arrive

    
# print(snail(100, 5, 2))

# change = 67000

# print(change % 50000)  # 50,000원 지폐
# ten_count = (change % 50000) // 10000  # 10,000원 지폐
# five_count = (change % 10000) // 5000  # 5,000원 지폐
# one_count = (change % 5000) // 1000  # 1,000원 지폐

# 1부터 사용자가 입력한 양의 정수까지의 총합을 구하는 코드를 작성하시오.
# n = 0
# total = 0
# user_input = int(input())

# while n <= user_input: #3 1 2
#     total += n # 0 + 0, 0 + 1, 1 + 2
#     n += 1 # 0 + 1, 1+1 =2, 2 + 1 =3

# print(total)

# members = ['민희', '영희', '철수']
# for idx, member in enumerate(members, start=1):
# 	print(idx, member)

# def T():
#     print("트루")
#     return True

# def F():
#     print("펄쓰")
#     return False


# if T() and T():
#     print("이거나옴?")

# if T() and F():
#     print("이거나옴?")

# if F() and T():
#     print("이거나옴?")

# if F() and F():
#     print("이거나옴?")

# if T() or T():
#     print("이거나옴?")

# if T() or F():
#     print("이거나옴?")

# if F() or T():
#     print("이거나옴?")

# if F() or F():
#     print("이거나옴?")



# arr = [1,2,3]

# if T() and arr[5]:
#     print("이거 에러나나나?")

# if F() and arr[5]:
#     print("이거 에러나나나?")

# if arr[5] and T():
#     print("이거 에러나냐/")

# if arr[5] and F():
#     print("이거 에러나냐/")

# dusts = {'서울' : 72, '대전' : 82, '구미' : 29, '광주' :45}
# result = {}
# for key, value in dusts.items():
    
#     if value > 70:
#         result[key] = value

# print(result)

# a = 10
# def func1():
#
#     global a
#     a = 3
#
# print(a)


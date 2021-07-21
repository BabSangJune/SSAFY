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


def my_avg(*num):
    num_avg = 0
    for i in num:
        num_avg += i
    return num_avg / len(num)



print(my_avg(77, 83, 95, 80, 70)) #81.0

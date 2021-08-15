a1 = '삼성청년소프트웨어아카데미'
list_a1 = list(a1)
N = len(list_a1)
list_empty = [0] * N

#swap
for i in  range(N//2):
    list_a1[i], list_a1[N-1-i] = list_a1[N-1-i], list_a1[i]

print(''.join(list_a1))

#슬라이싱
a2 = a1[::-1]

#뒤에서 부터 읽기
for i in range(len(a1)-1, -1, -1):
    print(a1[i], end='')

#reversed 함수
print(''.join(reversed(a1)))


"""
연습장
"""

n = int(input('가로 n : '))
m = int(input('세로 m : '))

# print((('*' * n) + '\n') * m)
# # print('*' * n + '\n' + '*' * m) #이래서 안나옴

for i in range(m): #세로(행) i 한번 반복시
    for j in range(n): #가로(열) j 전체 반복복
        print('*', end='')
    print() # end 사용 후 print 문으로 출력
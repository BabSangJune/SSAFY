"""
16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit씩 묶어 십진수로
변환하여 출력해보자
"""

h_to_b = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
hexadecimal = input()
bi = ''
result = []

for i in hexadecimal:
    if '0' <= i <= '9':
        temp = int(i)
    else:
        temp = h_to_b[i]

    n = 8
    for _ in range(4):
        if temp & n:
            bi += '1'
        else:
            bi += '0'
        n >>= 1

for i in range(0, len(bi), 7):
    result.append(int(bi[i:i+7], 2))

print(bi)
print(result)
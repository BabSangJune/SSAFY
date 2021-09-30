"""
0과 1로 이루어진 1차 배열에서 7개 byte를 묶어서 10진수로 출력하기
00000010001101 이면
1, 13 출력
"""

binary = input()

result = []



for i in range(0, len(binary), 7):
    result.append(int(binary[i:i+7], 2))

print(result)

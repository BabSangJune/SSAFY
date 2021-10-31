"""
날짜 : 2021.09.30
학습 : SWEA D5
제목 : [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드 D3
문제 :
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AXqt1_t66PIDFATi&contestProbId=AV15JEKKAM8CFAYD&probBoxId=AXw0bMRKDR0DFASZ&type=PROBLEM&problemBoxTitle=Start_%EC%8B%A4%EC%8A%B5_210930&problemBoxCnt=4
"""
import sys

sys.stdin = open("1242.txt", 'r')

password = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

h_to_d = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    #코드 입력
    code = ''
    for _ in range(N):
        tmp_code = input()
        for i in range(0, len(tmp_code)-1):
            #전부 0이면 코드 아니니까 pass
            if tmp_code[i] == '0':
                continue
            #찾으면 code에 넣어서
            else:
                code = tmp_code

    bi = ''
    for i in code:
        if '0' <= i <= '9':
            temp = int(i)
        else:
            temp = h_to_d[i]

        n = 8
        for _ in range(4):
            if temp & n:
                bi += '1'
            else:
                bi += '0'
            n >>= 1

    #진짜 암호 찾기
    real_pass = ''
    #뒤에서부터 1 찾으면 56자리
    for i in range(len(bi)-1, -1, -1):
        if bi[i] == '1':
            real_pass = bi[i-55:i+1]
            break
    print(real_pass)
    #검증
    change_code = []
    #7개씩 쪼개서 위의 암호랑 대조하고 저장
    for i in range(0, len(real_pass), 7):
        tmp_num = password[real_pass[i:i+7]]
        change_code.append(tmp_num)

    odd = 0
    even = 0
    
    #홀 짝 나누기
    for i in range(len(change_code)-1):
        if i % 2 == 0:
            odd += change_code[i]
        else:
            even += change_code[i]
    
    #연산
    tot = (odd * 3) + even + change_code[-1]

    result = 0
    #진짜 코드 검증
    if tot % 10 == 0:
        for i in change_code:
            result += i

    else:
        result = 0

    print('#{} {}'.format(tc, result))
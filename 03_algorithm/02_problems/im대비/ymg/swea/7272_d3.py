"""
날짜 : 2021.08.29
학습 : SWEA D3
제목 : 7272. 안경이 없어!
문제 :
어느 날 경근이는 알파벳 대문자로 이루어진 두 문자열을 비교해야 했는데, 이 날은 공교롭게도 안경이 없었다.
경근이는 매우 눈이 나빠서 안경을 벗으면 문자열을 문자 단위로 구별할 수는 있지만, 두 문자가 정확히 같은 지는 알지 못한다.
특히 알파벳 대문자 같은 경우 문자에 나 있는 구멍의 개수가 같으면 같은 문자이고, 다르면 다른 문자라고 생각한다.
예를 들어 구멍이 하나도 없는 CEFGHIJKLMNSTUVWXYZ들을 같은 문자로 생각하고,
구멍이 한 개 나 있는 ADOPQR들을 같은 문자로 생각하며,
구멍이 두 개 나 있는 유일한 문자 B는 유일하게 정확히 알 수 있다.
알파벳 대문자로 이루어진 두 문자열이 주어졌을 때, 경근이는 두 문자열이 같다고 판별하는지 다르다고 판별할 것인가?

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 두 문자열이 공백 하나로 구별되어 주어진다.
각 문자열은 알파벳 대문자 만으로 이루어져 있으며, 길이는 10이하이다.

[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
경근이가 주어진 두 문자열을 같은 것으로 생각하면 “SAME”을, 다른 것으로 생각하면 “DIFF”를 출력한다.
"""
import sys
sys.stdin = open("7272.txt", 'r')

T = int(input())
for tc in range(1, T + 1):
    words_1, words_2 = map(str, input().split())
    same_lst_A = 'ADOPQR'
    same_lst_B = 'CEFGHIJKLMNSTUVWXYZ'
    result = 'DIFF'

    for i in range(len(words_1)):
        if words_1[i] in same_lst_A:
            words_1 = words_1.replace(words_1[i], 'A')

    for i in range(len(words_2)):
        if words_2[i] in same_lst_A:
            words_2 = words_2.replace(words_2[i], 'A')

    for i in range(len(words_1)):
        if words_1[i] in same_lst_B:
            words_1 = words_1.replace(words_1[i], 'A')

    for i in range(len(words_2)):
        if words_2[i] in same_lst_B:
            words_2 = words_2.replace(words_2[i], 'A')

    if words_1 == words_2:
        result = 'SAME'

    print('#{} {}'.format(tc, result))






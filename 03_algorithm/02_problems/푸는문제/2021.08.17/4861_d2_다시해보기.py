"""
날짜 : 2021.08.17
학습 : SWEA D2
제목 : 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문
문제 :
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.

예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

"""

# T = int(input()) #tc 갯수
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(input().split()) for _ in range(N)]
#
#     front_lst_r = []
#     end_lst_r = []
#     result = ''
#     for i in range(N):
#         front_lst_r += arr[i]
#
#     for i in range(N):
#         rev = front_lst_r[i][::-1]
#         end_lst_r += [rev]
#
#     for i in range(N):
#         if front_lst_r[i] == end_lst_r[i]:
#             result += front_lst_r[i]
#
#     front_lst_c = []
#     end_lst_c = []
#     for j in range(M):
#         empty_lst = ''
#         for i in range(N):
#             empty_lst += arr[i][0][j]
#         front_lst_c += [empty_lst]
#
#     for j in range(M):
#         rev = front_lst_c[j][::-1]
#         end_lst_c += [rev]
#
#     for j in range(M):
#         if front_lst_c[j] == end_lst_c[j]:
#             result += front_lst_c[j]
#
#     print('#{} {}'.format(tc, result))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    result = '' #결과 저장

    for i in range(N): #가로 확인
        for j in range(N - M + 1): #M길이 만큼씩 확인 (01234),(43210)
            if arr[i][j:j + M] == arr[i][j:j + M][::-1]:
                result += arr[i][j:j + M]


    for i in range(N): #세로 확인
        for j in range(N - M + 1):
            c_words = '' #세로 문자열 저장
            for k in range(M):
                c_words += arr[j+k][i] #세로 하나씩 불러와서 저장
            if c_words == c_words[::-1]:
                result += c_words

    print('#{} {}'.format(tc, result))

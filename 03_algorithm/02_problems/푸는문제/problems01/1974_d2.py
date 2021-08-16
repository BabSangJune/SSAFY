"""
날짜 : 2021.08.16
학습 : SWEA D2
제목 : 1974 .스도쿠 검증
문제 :
스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.




같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.



입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.


[제약 사항]

1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.

2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.


[입력]

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

다음 줄부터 각 테스트 케이스가 주어진다.

테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.


[출력]

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

T = int(input()) #tc 갯수

for tc in range(1, T+1):
    N, word_len = map(int, input().split()) #가로, 세로 길이 / 단어 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    cp_list = [] # 퍼즐 가로 세로 전체 저장 할 리스트

    for i in range(N): #가로 전부 cp_list에 저장
        empty_list = []
        for j in range(N):
            empty_list += [puzzle[i][j]]
        cp_list += [empty_list]

    for j in range(N): #세로 전부 cp_list에 저장
        empty_list = []
        for i in range(N):
            empty_list += [puzzle[i][j]]
        cp_list += [empty_list]


    result = 0
    for i in range(N+N): #cp_list 인덱스 접근
        cnt_one = 0

        for j in range(N):

            if cp_list[i][j] == 0: #0 이면 cnt_one 0으로 초기화
                cnt_one = 0

            elif cp_list[i][j] == 1: #1이면 cnt_one += 1
                cnt_one += 1

                if cnt_one == word_len:
                    result += 1

                elif cnt_one > word_len: #cnt_one word_len 이상일때
                    result -= 1 #result -1 cnt_one이 4이상일때의 3에도 result에 +1했으므로
                    cnt_one = 0 #cnt_one 초기화
                    continue #포문 돌아가기

    print('#{} {}'.format(tc, result))


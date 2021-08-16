"""
날짜 : 2021.08.10
학습 : 2021.08.10 수업
제목 : babyjin 게임
문제 :
0~9 사이의 숫자카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고,
3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.

그리고 6장의 카드가 run과 triplet으로만 구성된 경우를 baby-gin으로 부른다.

6자리의 숫자를 입력을 받아 baby-gin 여부를 판단하는 프로그램을 작성하라.

베이비진이 맞다면 1을 아니라면 0을 출려하여라...

입력
첫줄에는 테스트케이스 개수가 주어지고, 이후 6장의 카드가 주어진다.
3
667767
054060
101123

출력
#1 1
#2 1
#3 0
#(테케번호) (정답) 형식으로 출력할것.
"""

T = int(input())


for tc in range(1, T+1):
    # 완전탐색
    nums = list(input())
    for i in range(6):
        for j in range(6):
            if j != i:
                for k in range(6):
                    if k != j and k != i:
                        for l in range(6):
                            if l != k and l != j and l != i :
                                for m in range(6):
                                    if m != l and m != k and m != j and m != i:
                                        for n in range(6):
                                            if n != m and n != l and n != k and n != j and n != i:
                                                print(nums[i], nums[j], nums[k], nums[l], nums[m], nums[n])

"""
날짜 : 2021.08.28
학습 : SWEA D3
제목 : 6190. 정곤이의 단조 증가하는 수
문제 :
정곤이는 자신이 엄청난 수학자임을 증명하기 위해, 어떤 규칙 만족하는 수를 찾아보기로 했다.
그 규칙은 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.
어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수이다.
예를 들어 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.
양의 정수 N 개 A1, …, AN이 주어진다.
 1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력하는 프로그램을 작성하라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤N ≤ 1,000) 이 주어진다.
두 번째 줄에는 N개의 정수 A1, …, AN(1 ≤ Ai ≤ 30,000) 이 공백 하나로 구분되어 주어진다.

[출력]
각 테스트 케이스마다 단조 증가하는 수인 Ai x Aj중에서 그 최댓값을 출력한다.
만약 Ai x Aj중에서 단조 증가하는 수가 없다면 -1을 출력한다.
"""
import sys

sys.stdin = open("6190.txt", 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    nums = list(map(int, input().split()))

    cnt_nums = []
    result = -1
    for i in range(N-1):
        # print(i)
        for j in range(i, N):
            if i != j:
                num = nums[i] * nums[j]
                cnt_nums.append(num)

    cnt_nums.sort()
    flag = False
    for i in range(len(cnt_nums)-1, -1, -1):
        if flag == True:
            break
        num = str(cnt_nums[i])
        tmp_num = []
        for j in range(len(num)):
            tmp_num.append(num[j])

        for k in range(len(tmp_num)):
            if 0 <= k < len(tmp_num)-1 and tmp_num[k] > tmp_num[k+1]:
                flag = False
                break

            else:
                flag = True

        if flag == True:
            result = int(num)
            break


    print('#{} {}'.format(tc, result))




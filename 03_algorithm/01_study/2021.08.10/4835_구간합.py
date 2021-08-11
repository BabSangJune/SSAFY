for tc in range(1, int(input()) + 1):
    # N : 정수 개수, M : 구간의 개수
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    # 제한 조거을 살펴보고 안거릴게 적당히
    max_value = 0
    min_value = 987654321

############################################
    # 충분히 머리속으로 그림 그려보기
    for i in range(N - M + 1):
        # 1
        tmp = 0
        for j in range(M):
            tmp += nums[i+j]

        # 2
        # for j in nums[i:i+M]:
        #     tmp += j

        # 3
        # tmp = sum(nums[i:i + M])

        if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp

    print("#{} {}".format(tc, max_value - min_value))

######################################################################
#  고오오오급 기술
# 그림을 떠올릴 것
for tc in range(1, int(input()) + 1):
    # N : 정수 개수, M : 구간의 개수
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    # 초기값 세팅
    tmp = 0
    for i in range(M):
        tmp = nums[i]

    max_value = min_value = tmp
    #중복연산을 하지 않음
    for i in range(M, N):
        tmp = tmp + nums[i] - nums[i - M]

        if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp

    print("#{} {}".format(tc, max_value - min_value))

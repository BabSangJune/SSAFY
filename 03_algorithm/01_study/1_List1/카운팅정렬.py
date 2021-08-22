T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    # 정렬하기
    sort_nums = [0] * N
    K = -1
    for i in nums:
        if K < i: K = i
    # K = max(nums)
    # 카운팅 정렬 할때 필요한게 어떤게 있었나???
    # K라는 값은 주어진 nums에서 가장 큰 값 이라고 했죠?
    counts = [0] * (K + 1)

    # 카운팅 하기
    for i in range(len(nums)):
        counts[nums[i]] += 1

    # 누적합 counts 리스트
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]


    # 뒤에서 부터 nums를 읽어오면서 자리에 맞게끔 쇽쇽쓱싹쇽
    for i in range(len(nums) - 1, -1, -1):
        # 위치를 찾아보자.
        n = nums[i]
        counts[n] -= 1
        idx = counts[n]
        sort_nums[idx] = n

        # 교재버전
        # sort_nums[counts[nums[i]]-1] = nums[i]
        # counts[nums[i]] -= 1

    print("#{} {}".format(tc, sort_nums))

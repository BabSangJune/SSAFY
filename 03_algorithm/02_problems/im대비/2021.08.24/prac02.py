def is_exist(nums, num):

    cnt = 0
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if nums[i][j] == num:
                cnt += 1
                break

    return cnt



nums = [
    [3, 2, 1, 7],
    [1, 2, 3, 4],
    [7, 5, 2, 1]
]

print(is_exist(nums, 7))


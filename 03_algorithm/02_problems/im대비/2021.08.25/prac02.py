# def is_same(row):
#     for col in range(5):
#         if apart[0][col] != apart[row][col]:
#             return 0
#
#     return 1
#
#
# apart = [
#     [3, 2, 1, 7, 9],
#     [1, 2, 3, 4, 5],
#     [3, 2, 1, 7, 9],
#     [4, 3, 2, 1, 0],
#     [3, 2, 1, 6, 9],
#     [3, 2, 1, 7, 9]
# ]
# cnt = 0
# for row in range(1, 5 + 1):
#     ret = is_same(row)
#     if ret == 1:
#         cnt += 1


def is_same(row) :
    for col in range(5):
        if apart[0][col] != apart[row][col]:
            return 0

    return 1


apart = [
    [3,2,1,7,9],
    [1,2,3,4,5],
    [3,2,1,7,9],
    [4,3,2,1,0],
    [3,2,1,6,9],
    [3,2,1,7,9]
]
cnt = 0
for row in range(1,5+1) :
    flag = 0
    for col in range(5):
        if apart[0][col] != apart[row][col] :
            flag = 1
            break
    if flag == 0 :
        cnt += 1

print(cnt)
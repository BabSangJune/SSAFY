# word = 'ATCKB'
#
# for i in range(len(word)):
#     for j in range(i, len(word)):
#         print(word[j], end=' ')
#     print()
#
# for i in range(len(word), -1, -1):
#     for j in range(0, i):
#         print(word[j], end=' ')
#     print()

N = int(input())

lst_ = [0] * 6

for i in range(len(lst_)):
    lst_[i] = N
    N += 2

print(lst_)
import random

numbers = range(1, 46)
print(list(numbers))

lotto_number = random.sample(numbers, 6)
print(lotto_number)

# 다음주 공개 ㅋ
# [2, 20, 42, 24, 30, 3]
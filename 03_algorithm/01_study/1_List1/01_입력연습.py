# input() 문자열 한줄 통으로 입력이 된다.

# a = input()
# print(a, type(a))

# 정수 한개를 입력받고 싶다.
# T = int(input())

# for tc in range(1, T+1):
#     ans = 0
#     print("#{} {}".format(tc, ans))

# for tc in range(T):
#     ans = 0
#     print("#{} {}".format(tc+1, ans))

# for tc in range(1, int(input())+1):
#     ans = 0
#     print("#{} {}".format(tc, ans))
# 문제에서 첫줄에는 항상 test_case 개수가 주어지고
# 출력으로는 #tc_num ans

# 정수를 여러개 입력 받는 방법?
# 1 2 3 4 5

# a, b, c, d, e = map(int, input().split())
# print(a, b, c, d, e)

# a = map(int, input().split())
# print(a)

# for i in a:
#     print(i)

# a = list(map(int, input().split()))
# print(a)

#한줄짜리 문자열을 리스트로 바꾸고 싶을떄
# abcde
# a = list(input())
# print(a)

# 아래는 조금 곤란..
# a = [input()]
# print(a)


# a b c d e
# print(input().split())
# print(list(input().split()))

# 전제조건 : 한자리의 수만 활용한다.
# 123456789 입력 원소하나씩 정수로 리스트
arr = list(map(int, input()))
print(arr)

# 더 중요한 것은 2차원 리스트 입력... ㅎ



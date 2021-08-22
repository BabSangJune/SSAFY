
#일반적인 print를 확인하여 중간중간 결과 확인
def my_print(idx, N):
    print("#{}까지의 합은 {} 이다.".format(idx, N))

def my_sum(N):
    tmp = 0

    for i in range(1, N + 1):
        tmp += i
        my_print(i, tmp)

    return tmp


ans = my_sum(10)

print(ans)
# 디버거를 사용할때
# 1. 도대체 어디다가 breakpoint를 찍어야하는지
# 2. step over 는 뭐고
# 3. step into 는 뭐고
# 4. step out 은 뭔지 알고 사용하자
# 5. 내가 원하는 곳부터 시작 가능
# 6. 중간중간 내가 보고 싶은 변수를 이용해 결과도 볼 수 있음..


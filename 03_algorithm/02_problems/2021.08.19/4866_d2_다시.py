"""
날짜 : 2021.08.19
학습 : SWEA D2
제목 : 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사
문제 :
주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
#1 1
#2 1
#3 0
"""

def chk(data):
    stack = []
    for word in data:
        if word == '(' or word == '{': #여는 괄호 스택
            stack.append(word)
        elif word == ')' or word == '}': #닫는 괄호이면 ?
            if len(stack) == 0: #닫는 괄호가 나왔는데 스택이 0이니까 맞지않음 0 리턴
                return 0
            elif stack[-1] == '(' and word == ')': #마지막 스택이 열린 괄호고 닫는 괄호를 가져왔으니
                stack.pop()
            elif stack[-1] == '{' and word == '}': #괄호 닫기
                stack.pop()
            else: #이도 저도 아니면 0 출력 ex) (}
                return 0

    else: #다 돌았을때
        if len(stack): #남아 있으면 0 리턴
            return 0
        else:
            return 1

T =  int(input()) #tc 갯수

for tc in range(1, T+1):
    data = input()
    result = chk(data)

    print('#{} {}'.format(tc, result))

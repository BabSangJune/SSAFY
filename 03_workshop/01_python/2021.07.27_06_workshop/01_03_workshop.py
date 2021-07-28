"""
날짜 : 2021.07.27
학습 : SSAFY 01_03_workshop
제목 : 3. 숫자의 의미
문제 :
정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 
하나만 남기고 제거한 list를 반환하는 lonely 함수를 작성하시오. 
이때, 제거된 후 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지해야 한다.

입력 :
출력 :
"""

'''
lonely([1, 1, 3, 3, 0, 1, 1]) #[1, 3, 0, 1]
lonely([4, 4, 4, 3, 3]) # [4, 3]
'''
# 쌤꺼
# 이건 주의
arr = [1, 2, 3, 4, 5]
for i in range(len(arr)-1, 0 , -1):
    if arr[i-1] == arr [i]:
        pass
    #지우는 작업 remove든 pop이든 다 괜찮음
    #이거도 가능
    
  

def lonely(lst):
    answer = [lst[0]]
    for num in lst[1:]:
        if num == answer[-1]:
            continue
        else:
            answer.append(num)
    return answer

print(lonely([1, 1, 3, 3, 0, 1, 1])) #[1, 3, 0, 1]
print(lonely([4, 4, 4, 3, 3])) # [4, 3]
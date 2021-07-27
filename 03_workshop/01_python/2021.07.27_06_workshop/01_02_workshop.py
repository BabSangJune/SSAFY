"""
날짜 : 2021.07.27
학습 : SSAFY 01_02_workshop
제목 : 2. 소대소대
문제 :
문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록
변환하여반환하는 low_and_up 함수를 작성하시오.
이때, 전달 받는 문자열은 알파벳으로만구성된다.

입력 :
출력 :
"""

'''
low_and_up('apple') # aPpLe
low_and_up('banana') # banana
'''


def low_and_up(word):
    result = ''
    for i in range(len(word)):
        if i % 2 == 1:
            result += word[i].upper()
        if i % 2 == 0:
            result += word[i]

    return result


print(low_and_up('apple'))
print(low_and_up('banana'))
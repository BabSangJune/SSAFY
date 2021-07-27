"""
날짜 : 2021.07.22
학습 : SSAFY 01_03_workshop
제목 : 3. 강한 이름
문제 :
문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하여
더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.

입력 :
출력 :
"""

def get_strong_word(word1, word2):
    tot1 = 0
    tot2 = 0
    for i in range(len(word1)):
        tot1 += ord(word1[i])

    for j in range(len(word2)):
        tot2 += ord(word2[i])

    if tot1 > tot2:
        return word1
    else:
        return word2



print(get_strong_word('z', 'a')) #'z'
print(get_strong_word('tom', 'john')) #'john'
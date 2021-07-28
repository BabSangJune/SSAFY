"""
날짜 : 2021.07.27
학습 : SSAFY 01_01_workshop
제목 : 1. 무엇이 중복일까
문제 :
문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 
반환하는 duplicated_letters 함수를 작성하시오.

입력 :
출력 :
"""
'''
duplicated_letters('apple') #['p']
duplicated_letters('banana') #['a', 'n']
'''

#쌤꺼 1 set 이용 중복 처리
# def duplicated_letters(words):
#     ans = []

#     for word in words:
#         if words.count(word) > 1:
#             ans.append(word)

#     return list(set(ans))

def duplicated_letters(words):
    ans = []
    for word in words:
        if words.count(word) > 1 and word not in ans:
            ans.append(word)

    return ans

    # return list({word for word in words if words.count(word) > 1})

#내꺼
# def duplicated_letters(letter): #set으로 만들어서, if 하나 더 result 알파벳이 있으면 안넣는다.
#     result = []
#     for i in letter:
#         if letter.count(i) >= 2:
#             if i in result:
#                 continue
#             else:
#                 result += i
#     return result


    # print(result)


# 못푼거
# def duplicated_letters(letter):
#     result = []
#     for j in letter:
#         result += j
#
#     for i in letter:
#         if letter.count(i) == 1:
#             result.remove(i)
#             continue
#
#             return result

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))
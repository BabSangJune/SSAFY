"""
날짜 : 2021.07.21
학습 : SSAFY 01_02_workshop
제목 : 2. Dictionary로 이루어진 List의 합 구하기
문제 :
Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value
들의 합을 반환하는 dict_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고
작성하시오.

입력 :
출력 :
"""

def dict_list_sum(dic_list):
    age_tot = 0
    for i in dic_list:
        age_tot += i['age']
    return age_tot


print(dict_list_sum([{'name': 'kim', 'age': 12},
                     {'name': 'lee', 'age': 4}]))
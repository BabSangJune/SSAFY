"""
날짜 : 2021.07.22
학습 : SSAFY 01_01_workshop
제목 : 2. 혈액형 분류하기
문제 :
여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아, 
key는 혈액형의종류, value는 사람 수인 dictionary를 반환하는 
count_blood 함수를 작성하시오.

입력 :
출력 :
"""

def count_blood(blood_list) :
    print(blood_list.count('A'))
    blood_type ={}
    blood_type['A'] = blood_list.count('A')
    blood_type['B'] = blood_list.count('B')
    blood_type['O'] = blood_list.count('O')
    blood_type['AB'] = blood_list.count('AB')

    return(blood_type)



print(count_blood([
    'A','B', 'A', 'O','AB','AB',
    'O','A','B','O','B','AB'
]))
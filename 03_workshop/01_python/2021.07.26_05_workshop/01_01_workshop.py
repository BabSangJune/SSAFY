"""
날짜 : 2021.07.26
학습 : SSAFY 01_01_workshop
제목 : 1. 평균 점수 구하기
문제 :
key 값으로 과목명, value 값으로 점수를 가지는 dictionary를 전달 받아, 
전체 과목의평균 점수를 반환하는 함수 get_dict_avg 함수를 작성하시오.

입력 :
출력 :
"""

def get_dict_avg(dic) :
    tot = 0
    cnt = 0
    for score in dic.values() :
        tot += score
        cnt += 1
    return tot/cnt
    
def get_dict_avg2(dic) :
    tot = 0
    
    for score in dic.values() :
        tot += score
        
    return tot / len(dic)
    


print(get_dict_avg({
    'python' : 80,
    'algorithm' : 90,
    'django' : 89,
    'web' : 83
}))
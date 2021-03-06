"""
날짜 : 2021.08.15
학습 : SWEA D4
제목 : 1206 .[S/W 문제해결 기본] 1일차 - View
문제 :
강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.

이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만 왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.

그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.

빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.

아래와 같이 강변에 8채의 빌딩이 있을 때, 연두색으로 색칠된 여섯 세대에서는 좌우로 2칸 이상의 공백이 존재하므로 조망권이 확보된다. 따라서 답은 6이 된다.



A와 B로 표시된 세대의 경우는 왼쪽 조망은 2칸 이상 확보가 되었지만 오른쪽 조망은 한 칸 밖에 확보가 되지 않으므로 조망권을 확보하지 못하였다.

C의 경우는 반대로 오른쪽 조망은 2칸이 확보가 되었지만 왼쪽 조망이 한 칸 밖에 확보되지 않았다.

[제약 사항]

가로 길이는 항상 1000이하로 주어진다.

맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다. (예시에서 빨간색 땅 부분)

각 빌딩의 높이는 최대 255이다.

[입력]

입력 파일의 첫 번째 줄에는 테스트케이스의 길이가 주어진다. 그 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트케이스가 주어진다.
100
0 0 225 214 82 73 241 233 179 219 135 62 36 13 6 71 179 77 67 139 31 90 9 37 ...
1000
0 0 225 214 82 73 241 233 179 219 135 62 36 13 6 71 179 77 67 139 31 90 9 37 ...
[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 조망권이 확보된 세대의 수를 출력한다.
#1 691
#2 9092
"""
'''
해결 방안
맨앞 2개 맨뒤 2개 인덱스엔 건물 없음
한 건물 지점 앞 2개 건물 뒤 2개 건물 현재와 비교하여 현 건물보다 작은지 확인
모두 작으면 현재 건물 높이 - 4개 중 가장 큰 건물 높이하고 그 값을 누적
'''

# T = int(input())
for tc in range(1, 11): #총 10개 test 케이스
    area = int(input()) #지역 크기
    bdgs = list(map(int, input().split())) #빌딩 높이 리스트
    cnt = 0 #조망권 확보 갯수 누적할 변수


    for i in range(2, len(bdgs)-2): #양쪽 -2 idx 빼고

        if bdgs[i] > bdgs[i-2] and bdgs[i] > bdgs[i-1] and bdgs[i] > bdgs[i+1] and bdgs[i] > bdgs[i+2]:
            high_bdg = 0
            for j in [i+2, i+1, i-2, i-1]:

                if high_bdg < bdgs[j]: #이러면 인덱스를 들고오니까 ..
                    high_bdg = bdgs[j]

            cnt += bdgs[i] - high_bdg

    print('#{} {}'.format(tc, cnt))

'''
초기화 위치 잘 찾기
cnt 위치
인덱스 가지고와서 가장 큰 건물 들고와야하는데 엉뚱하게 들고옴
'''



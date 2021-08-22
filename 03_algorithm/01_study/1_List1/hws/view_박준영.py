for case in range(10):  # case 10
    T = int(input())  # case 입력
    B = list(map(int, input().split()))  # 빌딩 리스트
    ans = 0  # 답

    for i in range(2, T - 2):  # 인덱스 에러 방지
        max_B = 0  # 빌딩의 최대값
        if B[i] > B[i - 1] and B[i] > B[i - 2] and B[i] > B[i + 1] and B[i] > B[i + 2]:  # 양옆의 2개의 건물보다 크고
            for j in (B[i - 2], B[i - 1], B[i + 1], B[i + 2]):  # 양옆 4건물 중
                if max_B < j:  # 제일 큰건물을 저장
                    max_B = j
            ans += B[i] - max_B  # 결과에 차이만큼 추가
    print(f'#{(case + 1)}  {ans}')
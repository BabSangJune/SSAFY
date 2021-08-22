T = int(input())

for tc in range(1, T+1):
    # K: 이동할 수 있는 거리
    # N: 마지막 종점의 위치 (0번 정류장 부터 출발)
    # M: 충전소의 개수
    K, N, M = map(int, input().split())

    charge = list(map(int, input().split()))

    bus_stop = [0] * (N+1)

    #충전소를 표시하자.!!!!!!
    # for i in charge:
    #     bus_stop[i] = 1

    for i in range(M):
        bus_stop[charge[i]] = 1

    bus_idx = 0 #버스의 위치
    ans = 0

    #무한루프 주의해야한다...
    while True:
        #버스가 이동할 수 있는 만큼 무조건 가
        bus_idx += K
        if bus_idx >= N: break # 종점에 도착하거나 종점을 지나는 경우이므로 끝

        for i in range(bus_idx, bus_idx - K, -1):
            # 충전소 있다면 갱신
            # if bus_stop[i] == 1:
            if bus_stop[i]:
                ans += 1
                bus_idx = i
                break
        #충전기를 못찾았을떄        
        else:
            ans = 0
            break


    print("#{} {}".format(tc, ans))
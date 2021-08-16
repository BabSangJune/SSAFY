T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stu = []
    room = [0] * 201
    for i in range(N):
        a = list(map(int, input().split()))
        stu.append(a)
        a[0] = (a[0] + 1) // 2
        a[1] = (a[1] + 1) // 2


    for k in stu:
        if k[0] > k[1]:
            k[0], k[1] = k[1], k[0]
        for j in range(k[0], k[1] + 1):
            room[j] += 1

    max = 0
    for m in room:
        if m > max:
            max = m

    print("#{} {}".format(tc , max))
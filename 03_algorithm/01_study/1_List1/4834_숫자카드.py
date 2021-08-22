for i in range(1, int(input()) + 1):
    N = input()

    card = list(map(int, input()))
    # print(card)
    counting = [0] * 10

    cnt = 0 #카드 번호
    max_value = 0 #카드 갯수

    max_count = 0
    ans_idx = -1
    #카운팅을 했다...
    for k in card:
        counting[k] += 1
######################################################################################
#이 부분은 한번 충분히 생각해 볼것
        if counting[k] >= max_count:
            max_count = counting[k]
            ans_idx = k

    print(ans_idx, max_count)
    # 요거 되나안되나??????????
    # for j in range(len(counting)-1,-1,-1):
    #     if counting[j] == max_count:
    #         max_value = counting[j]
    #         cnt = j
    #         break

###################################################################################


    # for j in range(len(counting) - 1, -1, -1):
    #     #요기에 등호는 앞에서부터 접근했다면 필요함.
    #     #뒤에서부터 했으니 필요없음..
    #     if counting[j] > max_value:
    #         max_value = counting[j]
    #         cnt = j

    # print('#{} {} {}'.format(i, cnt, max_value))
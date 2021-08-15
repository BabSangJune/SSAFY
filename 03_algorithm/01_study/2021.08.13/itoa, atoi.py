def itoa(a_int): #정수를 문자로
    tmp = a_int
    tmp_one = 0
    tmp_list = []

    for _ in range(a_int):
        if tmp == 0: #0이면 스탑
            break
        elif tmp != 0: #0이 아니면 ㄱㄱ
            tmp_one = tmp % 10 #4
            tmp = tmp // 10
            tmp_list = [tmp_one] + tmp_list

    return tmp_list



def atoi(a_str): #문자를 정수로
    pass


a1 = '1234'
a2 = 1230

print(itoa(a2))

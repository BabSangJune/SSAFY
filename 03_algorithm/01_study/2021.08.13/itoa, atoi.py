# def itoa(a_int): #정수를 문자로
#     tmp = a_int
#     tmp_one = 0
#     tmp_list = []
#
#     for _ in range(a_int):
#         if tmp == 0: #0이면 스탑
#             break
#         elif tmp != 0: #0이 아니면 ㄱㄱ
#             tmp_one = tmp % 10 #4
#             tmp = tmp // 10
#             tmp_list = [tmp_one] + tmp_list
#
#     return tmp_list
#
#
#
# def atoi(a_str): #문자를 정수로
#     int_text = 0
#     for txt in range(len(a_str) - 1, -1, -1):  # 3 2 1 0
#         text_ascii = ord(a_str[txt]) - 48
#         print(text_ascii)
#         int_text += text_ascii * (10 ** (len(a_str) - 1 - txt))
#
#     return int_text


def atoi(str_input: str) -> int:
    ans = 0
    for i in range(len(str_input)):
        ans *= 10
        ans += ord(str_input[i]) - ord('0')

    # 양수만을 위한 코드 / 음수면 ????
    return ans

def itoa (int_input: int) -> str:
    ans = ''
    tmp = int_input

    #이러면 1부터 들어와서 거꾸로 들어옴
    while tmp > 0:
        num = tmp % 10
        ans += chr(num + 48) #= + ans
        tmp //= 10

    return tmp


a1 = '1234'
a2 = 1230

print(itoa(a2))

def f2():
    print("f2시작")
    print("f2끝")


def f1():
    print("f1시작")

    print(f2())
    print("f1끝")
    return "낄낄"


print("main시작")
print(f1())
print("main끝")

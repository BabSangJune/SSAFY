dust = 90

if dust > 150:
    print("매우나쁨")
else:
    if dust > 80:
        print("나쁨")
    else:
        if dust > 30:
            print("보통")
        else:
            print("좋음")

#elif 순서가 굉장히 중요하다. 
if dust > 150:
    print("매우나쁨")
elif dust > 80:
    print("나쁨")
elif dust > 30:
    print("보통")
else:
    print("좋음")


##############################
if dust > 150:
    print("매우나쁨")
elif 80 >= dust > 30:
    print("보통")
elif 150 >= dust > 80:
    print("나쁨")
else:
    print("좋음")

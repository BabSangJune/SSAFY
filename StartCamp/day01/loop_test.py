number = [78,24,2,33,25,32,86,2558]


#리스트이 요소로 접근하여 값을 가지고 온다. 
# for i in number:
#     print(i)

# #리스트의 인덱스로 접근하기 위해서는
for i in range(len(number)):
    print(number[i])

print(len(number))
print(range(len(number)))
print(list(range(len(number))))

#range
#range(끝값+1)
#range(시작값, 끝값+1)
#range(시작값, 끝값+1, step)


n = 0
while n < 3:
    print(n) 
    n += 1

def is_same(lst1, lst2):
    for i in range(len(lst1)):
        if a[i] != b[i]:
            return False

    return True



a = [3, 2, 7, 5, 9]
b = [3, 2, 7, 5, 9]

result = is_same(a, b)
print(result)
X = int(input())

for i in range(-300, 300, 1):
    for j in range(-300 , 300, 1):
        if i ** 5 - j ** 5 == X:
            print(i, end = ' ')
            print(j)
            break
    else:
        continue
    break
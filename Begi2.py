judge = False
N, yen = map(int, input().split())
N2 = N
oriN = N
while N >= 0:
    x = N
    N -= 1
    N2 = oriN
    while N2 - N >= 0:
        y = N2 - N
        N2 -= 1
        z = oriN - x - y
        if 10000 * x + 5000 * y + 1000 * z == yen:
            judge = True
            break
    else:
        continue
    break

if judge == True:
    print(x, y ,z)
else:
    print(-1, -1, -1)
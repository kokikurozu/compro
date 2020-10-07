a = [1, 1, 2]
rank = 20
for j in range(rank-3):
    gokei = 0
    for i in range(3):
        gokei += a[i + j]
    a.append(gokei)
print(a[-1] * 100)
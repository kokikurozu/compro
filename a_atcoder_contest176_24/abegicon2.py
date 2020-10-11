N = input()
gokei = 0
for i in N:
    gokei += int(i)

print('YNeos'[gokei%9!=0::2])
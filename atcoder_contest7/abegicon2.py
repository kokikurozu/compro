n = input()
ai = list(map(int, input().split()))
gokei = 0

for i in ai:
    if i % 6 == 2 or i % 6 == 4:
        gokei += 1
    elif i % 6 == 5:
        gokei += 2
    elif i % 6 == 0:
        gokei += 3

print(gokei)
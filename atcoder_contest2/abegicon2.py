X = int(input())
uresisa = 0
while True:
    if X >= 500000:
        X -= 500000
        uresisa += 1000000
    else:
        break

while True:
    if X >= 500:
        X -= 500
        uresisa += 1000
    else:
        break
while True:
    if X >= 5:
        X -= 5
        uresisa += 5
    else:
        break

print(uresisa)
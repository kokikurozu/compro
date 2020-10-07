S = list(str(input()))
max1 = 0
now_max = 0
for i in S:
    if i == "R":
        max1 += 1
        if now_max < max1:
            now_max = max1
    elif i == "S":
        if now_max < max1:
            now_max = max1
        max1 = 0

print(now_max)
H = int(input())
cnt = 1

while True:
    cnt *= 2
    if H < cnt:
        break
print(cnt - 1)
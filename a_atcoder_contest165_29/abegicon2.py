X = int(input())
bank = 100
cnt = 0
while True:
    cnt += 1
    bank = int(bank * 1.01)
    if bank >= X:
        break
print(cnt)
from decimal import Decimal

X = int(input())
bank = 100
cnt = 0
while True:
    cnt += 1
    bank = int(bank * 101)
    bank = bank // 100
    if bank >= X:
        break
print(cnt)
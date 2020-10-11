K = int(input())
amari = 7
count = 0
Is_finish = 0
for i in range(1000000):
    amari = amari % K
    if amari == 0:
        Is_finish = 1
        break
    amari = amari * 10 + 7
if Is_finish:
    print(i + 1)
else:
    print(-1)
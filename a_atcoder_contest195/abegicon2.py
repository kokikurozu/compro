a,k = map(int,input().split())
ans = 0
if k == 0:
    ans = 2 * (10 ** 12) - a
else:
    for i in range(10000000):
        ans += 1
        a = a + 1 + a * k
        if a >= 2 * (10 ** 12):
            break
print(ans)
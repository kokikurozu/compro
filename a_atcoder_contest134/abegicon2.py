n,d = map(int,input().split())
cnt = 0
for i in range(10):
    cnt += 1
    n = n - (1 + 2 * d)
    if n <= 0:
        break
print(cnt)
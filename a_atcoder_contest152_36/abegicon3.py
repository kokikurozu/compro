N = int(input())
Pi = list(map(int,input().split()))
cnt = 0
min_now = 3 * 10 ** 5
for i in Pi:
    if i <= min_now:
        min_now = i
        cnt += 1

print(cnt)
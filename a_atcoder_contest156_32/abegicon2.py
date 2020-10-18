N, K = map(int,input().split())
cnt = 0
while True:
    N = N // K
    cnt += 1
    if N == 0:
        break

print(cnt)
N = int(input())
pi = list(map(int,input().split()))
cnt = 0

for i in range(N):
    if pi[i] != i+1:
        cnt += 1
if cnt <= 2:
    print('YES')
else:
    print('NO')
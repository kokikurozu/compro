N, M, K = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int,input().split()))
minute = 0
cnt = 0
for i in A:
    minute += i
    cnt += 1
    if minute > K:
        minute -= i
        cnt -= 1
        max_cnt = cnt
        lasti = cnt
        break

if cnt == len(A):
    lasti = cnt
    max_cnt = cnt

for j in B:
    if minute > K:
        cnt -= 1
        max_cnt = max(max_cnt, cnt)
        break
    minute += j
    cnt += 1
    if minute <= K:
        max_cnt = max(max_cnt, cnt)
    if minute > K:
        for k in range(lasti):
            minute -= A[lasti]
            cnt -= 1
            lasti -= 1
    if minute < K:
        max_cnt = max(max_cnt, cnt)

print(max_cnt)
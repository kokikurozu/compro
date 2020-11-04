from bisect import *

N, M = map(int,input().split())

Hi = list(map(int,input().split()))
Wi = list(map(int,input().split()))
Hi.sort()


sum1 = [Hi[i + 1] - Hi[i] for i in range(N - 1)]
sum2 = sum1[1::2] + [0]
sum3 = [0] + sum1[::2]

for i in range(len(sum3) - 1):
    sum3[i + 1] += sum3[i]
for i in range(len(sum2) - 1, 0, -1):
    sum2[i - 1] += sum2[i]

ans = 1 << 60

for w in Wi:
    x = bisect(Hi, w)
    if x % 2:
        x -= 1
    cost = sum1[x // 2] + sum2[x // 2] + abs(Hi[x] - w)
    if ans > cost:
        ans = cost
 
print(ans)
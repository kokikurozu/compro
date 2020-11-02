from bisect import *

N = int(input())
L = list(map(int,input().split()))

L.sort()
cnt = 0

for i in range(len(L)-1,1,-1):
    for j in range(i-1, 0, -1):
        x = bisect_right(L,L[i] - L[j])
        if j > x:
            cnt += j - x

print(cnt)
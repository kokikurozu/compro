N = int(input())
hi = list(map(int,input().split()))
Is = 1
for i in range(1,N):
    if hi[i] - hi[i-1] >= 1:
        hi[i] -= 1
    elif hi[i] - hi[i-1] < 0:
        Is = 0
        break
if Is == 1:
    print('Yes')
else:
    print('No')
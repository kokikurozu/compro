N = int(input())
hi = list(map(int,input().split()))
Is = 1
for i in range(1,N):
    if hi[i] - hi[i-1] >= 0:
        pass
    elif hi[i] - hi[i-1] == -1:
        hi[i] -= 1
    else:
        Is = 0
        break
    hi[N-1]
if Is == 1:
    print('Yes')
else:
    print('No')
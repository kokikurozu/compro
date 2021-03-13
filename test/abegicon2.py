n,s,d = map(int,input().split())
xy=[list(map(int,input().split()))for _ in range(n)]
Is_flg = 0
for i,j in xy:
    if i < s and j > d:
        Is_flg = 1
        break
if Is_flg == 1:
    print('Yes')
else:
    print('No')
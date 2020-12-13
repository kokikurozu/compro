n,m,t = map(int,input().split())
ab=[list(map(int,input().split()))for _ in range(m)]
Is = 1
bt = n
cafe_out = 0
cafe_in = 0
for a,b in ab:
    bt -= a - cafe_out
    if bt <= 0:
        Is = 0
        break
    bt += b - a
    if bt >= n:
        bt = n
    cafe_out = b

bt -= (t - cafe_out)
if bt <= 0:
    Is = 0
if Is == 1:
    print('Yes')
else:
    print('No')
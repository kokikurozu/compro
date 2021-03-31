n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
min_money = 1000000000000
for a,p,x in xy:
    if a < x:
        min_money = min(min_money,p)
if min_money == 1000000000000:
    min_money = -1

print(min_money)
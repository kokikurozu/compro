N = int(input())
all_date = 366
date = [0 for _ in range(all_date)]
vac = [0 for _ in range(N)]
list_date = [0,31,29,31,30,31,30,31,31,30,31,30,31]
list_date_sum = [0,0,31,60,91,121,152,182,213,244,274,305,335,366]
for i in range(N):
    a,b = map(int,input().split('/'))
    date[list_date_sum[a] + b - 1] += 1
for j in range(all_date):
    if j % 7 == 0 or j % 7 == 6:
        date[j] += 1
cnt = 0
for k in range(all_date):
    if date[k] >= 1:
        cnt += date[k] - 1
        date[k] = 1
    if date[k] == 0 and cnt >= 1:
        cnt -= 1
        date[k] = 1

ans = 0
count_renkyu = 0
max_renkyu = 0
for l in range(all_date):
    if date[l] >= 1:
        count_renkyu += 1
        max_renkyu = max(max_renkyu,count_renkyu)
    if date[l] == 0:
        count_renkyu = 0
        max_renkyu = max(max_renkyu,count_renkyu)

print(max_renkyu)
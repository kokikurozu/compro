n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
x = {}
now_num = a[0]
count = 0
for i in range(n):
    if now_num == a[i]:
        count += 1
    else:
        x[now_num] = count
        count = 1
        now_num = a[i]

x[now_num] = count

now_count = k
ans = 0
now_number = 0
cnt = -1
for i,j in x.items():
    cnt += 1
    now_number = i
    if now_number != cnt:
        break
    now_count = min(j,now_count)
    ans += now_count
print(ans)
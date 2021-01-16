import collections
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
print(x)
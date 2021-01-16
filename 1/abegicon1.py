n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a_max = 0
now_max = 0
for i in range(n):
    new_i = a[i] * b[i]
    new_max_i = a_max * b[i]
    a_max = max(a_max,a[i])
    now_max = max(new_i,new_max_i,now_max)
    print(now_max)
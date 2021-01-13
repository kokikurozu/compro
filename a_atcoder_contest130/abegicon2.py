n,x = map(int,input().split())
li = map(int,input().split())
x_now = 0
cnt = 1
for i in li:
    x_now += i
    if x_now <= x:
        cnt += 1
    else:
        break
print(cnt)
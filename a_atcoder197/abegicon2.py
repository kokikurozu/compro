h,w,x,y = map(int,input().split())
s = [list(input()) for i in range(h)]
x = x-1
y = y-1
x_a = x
y_a = y
if s[x-1][y-1] == 1:
    ans = 0
else:
    ans = 1
for i in range(101):
    x_a += 1
    if x_a >= h:
        break
    if s[x_a][y] == '.':
        ans += 1
    else:
        break

x_a = x
for i in range(101):
    x_a -= 1
    if x_a < 0:
        break
    if s[x_a][y] == '.':
        ans += 1
    else:
        break

x_a = x
for i in range(101):
    y_a += 1
    if y_a >= w:
        break
    if s[x][y_a] == '.':
        ans += 1
    else:
        break

y_a = y
for i in range(101):
    y_a -= 1
    if y_a < 0:
        break
    if s[x][y_a] == '.':
        ans += 1
    else:
        break

print(ans)
a,b,x,y = map(int,input().split())
ans = 0
build = 'a'
cnt = a
goal = b
if a > b:
    cnt -= 1
    ans += x
    build = 'b'
while True:
    if cnt == goal and build == 'b':
        break
    elif build == 'a':
        ans += x
        build = 'b'
    else:
        if 2 * x < y:
            ans += 2*x
        else:
            ans += y
        if cnt < goal:
            cnt += 1
        if cnt > goal:
            cnt -= 1
print(ans)
a,b,x,y = map(int,input().split())
ans = 0
if a > b:
    a = a - 1
    ans += x
if 2 * x < y:
    ans += 2 * x * abs(a-b) + x
else:
    ans += y * abs(a-b) + x

print(ans)
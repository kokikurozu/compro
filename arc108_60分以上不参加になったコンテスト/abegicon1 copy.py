a,b,x,y = map(int,input().split())
ans = 0
if (a+b) % 2 == 1:
    if x <= y:
        ans += x * abs(a-b)
    elif x > y:
        ans += y * (abs(a-b) - 1)
        if 2 * x < y:
            ans += 2 * x
        else:
            ans += y

else:
    if x <= y:
        ans += x * (abs(a-b) - 1)
        if 2 * x < y:
            ans += 2 *  x
        else:
            ans += y
    elif x > y:
        ans += y * (abs(a-b) - 1) + x
print(ans)

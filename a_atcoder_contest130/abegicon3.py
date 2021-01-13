w,h,x,y = map(int,input().split())

ans = w*h/2

if w/2 == x and h/2 == y:
    ans2 = 1
else:
    ans2 = 0

print(ans,ans2)
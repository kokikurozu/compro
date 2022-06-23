a,b,c = map(int,input().split())
ans = c * (-(-a//c))
if ans <= b:
    print(ans)
else:
    print(-1)
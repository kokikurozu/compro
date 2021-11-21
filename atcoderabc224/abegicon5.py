r,x,y = map(int,input().split())
ans = ((x ** 2 + y ** 2) / r ** 2) ** 0.5
ans = -(-ans//1)
if x ** 2 + y ** 2 < r ** 2:
    print(2)
else:
    print(int(ans))

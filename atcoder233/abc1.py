x,y = map(int,input().split())
if x < y:
    print(-(-(y-x)//10))
else:
    print(0)
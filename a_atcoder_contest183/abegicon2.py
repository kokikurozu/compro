sx,sy,gx,gy = map(int,input().split())

a = (gx-sx)/(gy+sy)

ans = sx + sy*a
print(ans)
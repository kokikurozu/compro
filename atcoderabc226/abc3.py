r,x,y = map(int,input().split())
kyori = x ** 2 + y ** 2
#print(kyori)
ans = 0
for i in range(10000000000):
    k = (r * i) * (r * i)
    if kyori < k:
        break
print(i)
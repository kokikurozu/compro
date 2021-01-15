a,b = map(str,input().split())
ax = 0
bx = 0
for i in list(a):
    ax += int(i)
for j in list(b):
    bx += int(j)
if ax >= bx:
    print(ax)
else:
    print(bx)
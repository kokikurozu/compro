a = 0
n = int(input())
liX = []
liY = []
for i in range(n):
    x, y = map(int, input().split())
    liX.append(x)
    liY.append(y)
liX.sort()
liY.sort()
if n % 2 == 1:
    start = liX[int(n/2)]
    finish = liY[int(n/2)]
else:
    start = (liX[int(n/2)] + liX[int(n/2) - 1])/2
    finish = (liY[int(n/2)] + liY[int(n/2) -1])/2
goukei = 0
for j in liX:
    goukei += abs(j - start)
for k in liY:
    goukei += abs(k - liX[a])
    goukei += abs(finish - k) 
    a += 1
print(int(goukei))
n = int(input())
x = n
plus = 10000
while True:
    if x*(x+1)/2 < n+1:
        break
    x = x // 1.2
x = int((x+1) * 1.2)
while True:
    if x*(x+1)/2 < n+1:
        break
    elif x - 10000 > 0:
        x = x - 10000
    else:
        plus = x
        x = 0
x = x + plus
while True:
    if x*(x+1)/2 < n+1:
        break
    x = x - 1
if (x+1)*(x+2)/2 != n+1:
    x = x - 1
print(n - x)

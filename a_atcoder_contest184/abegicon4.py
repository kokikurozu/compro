a,b,c = map(int,input().split())
list_fukuro = [[[0 for _ in range(100)] for j in range(100)] for k in range(100)]
x = a/(a+b+c)
y = b/(a+b+c)
x = c/(a+b+c)
for i in range(99,0,-1):
    for j in range(99,0,-1):
        for k in range(99,0,-1):
            list_fukuro[i][j][k] = 2
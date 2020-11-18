k, x = map(int,input().split())
mini = x - (k - 1)
for i in range(mini , k+x, 1):
    print(i, end=" ")
N, X, T = map(int,input().split())
gokei = 0
time = 0
while True:
    gokei += X
    time += T
    if gokei >= N:
        break
print(time)
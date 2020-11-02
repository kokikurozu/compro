N = int(input())
d = list(map(int,input().split()))

recovery = 0

for i in range(N):
    for j in range(i+1, N, 1):
        recovery += (d[i] * d[j])
print(recovery)
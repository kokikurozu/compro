N = int(input())
Az = [0 for i in range(N)]
Ai = list(map(int, input().split()))

for i in Ai:
    Az[i-1] += 1
for j in Az:
    print(j)
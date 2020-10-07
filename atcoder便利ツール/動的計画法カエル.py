N = int(input())
listA = list(map(int, input().split()))

DP = [0] * N
DP[0] = 0
DP[1] = abs(listA[1] - listA[0])

for i in range(2, N ,1):
    dan2 = abs(listA[i] - listA[i-2]) + DP[i-2]
    dan1 = abs(listA[i] - listA[i-1]) + DP[i-1]
    DP[i] = min(dan2, dan1)

print(DP[N-1])
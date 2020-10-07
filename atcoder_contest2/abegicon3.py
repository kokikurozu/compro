K, N = map(int, input().split())
listA = list(map(int, input().split()))

listA.append(K + listA[0])
#listA.insert(0, listA[N -1])
max_now = 0

for i in range(N):
    kyori = abs(listA[i] - listA[i+1])
    max_now = max(max_now, kyori)

print(K - max_now)
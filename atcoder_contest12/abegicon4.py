import collections

N, M = map(int, input().split())
AB = [0] * M
ABrootcount = [N] * N
ABshirushi = [0] * N
print("Yes")
for i in range(M):
    AB[i] = map(int, input().split())
for j in AB:
    if j[0] == 1:
        AB[1] = 1
        ABshirushi[AB[1]] = 1
        ABrootcount[AB[1]] = 1
    elif j[1] == 1:
        ABshirushi[0] = 1
        ABshirushi[AB[0]] = 1
        ABrootcount[AB[0]] = 1

if collections.Counter(ABrootcount)[0] == 1:
    break
import collections
goukei = 0

N = int(input())
Ai = list(map(int, input().split()))
number = [j for j in range(1, N+1, 1)]
plus_Ai = [x + y for (x, y) in zip(Ai, number)]
minus_Ai = [x - y for (y, x) in zip(Ai, number)]
c = collections.Counter(plus_Ai)

for i in minus_Ai:
    goukei += c[i]
print(goukei)

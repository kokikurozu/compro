from math import sqrt
from itertools import combinations

N, D = map(int,input().split())
cnt = 0
listX = []
for j in range(N):
    listX.append(list(map(int,input().split())))

comb = list(combinations(listX, 2))

for i in comb:
    goukei = 0
    for m, n in zip(i[0], i[1]):
        goukei += (m - n) ** 2
    if sqrt(goukei) == int(sqrt(goukei)):
        cnt += 1
print(cnt)
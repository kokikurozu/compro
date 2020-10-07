import itertools
import math

N = int(input())
cnt = 0
listA = []
for i in range(3, int(math.sqrt(N)+1), 2):
    listA.append(i)
#print(listA)
listB = list(itertools.combinations(listA, 3))
#print(listB)
for listC in listB:
    seki = 1
    for x in listC:
        seki = seki * x
    if seki <= N:
        cnt += 1
print(cnt)

from itertools import product
import numpy as np

N, M = map(int, input().split())
liS_all = []
denkyuM = [0 for i in range(M)]
cnt = 0

for j in range(1, M + 1):
    liS = list(map(int, input().split()))
    denkyulist = [0 for k in range(N)]
    for l in liS[1:]:
        denkyulist[l-1] = 1
    liS_all.append(denkyulist)

liP = list(map(int, input().split()))

bit_list = list(product([0, 1], repeat = N))

for bit in bit_list:
    n = 0
    judge = True
    for denkyu in liS_all:
        ronriseki = np.logical_and(bit, denkyu)
        if sum(ronriseki) % 2 != liP[n]:
            judge = False
        n += 1
    if judge == True:
        cnt += 1
print(cnt)
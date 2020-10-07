import itertools
from math import sqrt
import numpy as np

kyorilist = []
matilist = []
N = int(input())
for i in range(N):
    matilist.append(map(int,input().split()))
lis = [x for x in range(N)] # 0からn-1までのリスト
 
permutations_lis = itertools.permutations(lis)# 全ての場合のリストを生成
# 以下出力
for one_case in permutations_lis:
    gokeikyori = 0 
    for num in range(1, len(one_case), 1):
        kyori = matilist[one_case[num]] - matilist[one_case[num + 1]]
        gokeikyori += sqrt(kyori[0] ** 2 + kyori[0] ** 2)
    kyorilist.append(gokeikyori)
print(np.average(kyori))
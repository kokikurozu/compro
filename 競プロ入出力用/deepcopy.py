from copy import deepcopy

#基本的な使い方
yi = [[0,1],[5,3],[6,4]]
yi_copy = deepcopy(yi)
yi_copy[0][1] = 100
print(yi_copy)
print(yi)


#以下deepcopyでないとどんな問題が起こるか

n = 3
xi = [[0,1],[5,3],[6,4]]
xi_copy = xi
xi_copy[0][1] = 100
print(xi_copy)
print(xi)
yi = [[0,1],[5,3],[6,4]]
yi_copy = deepcopy(yi)
yi_copy[0][1] = 100
print(yi_copy)
print(yi)
zi = [[0,1],[5,3],[6,4]]
zi_copy = [0 for i in range(n)]
for i in range(n):
    zi_copy[i] = zi[i]
zi_copy[0][1] = 100
print(zi_copy)
print(zi)
vi = [[0,1],[5,3],[6,4]]
vi_copy = [[] for _ in range(n)]
for i in range(n):
    for j in range(2):
        vi_copy[i].append(vi[i][j])
vi_copy[0][1] = 100
print(vi_copy)
print(vi)
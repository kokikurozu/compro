import itertools
n,m,l = map(int,input().split())
pqr = map(int,input().split())

list_all = list(itertools.permutations(pqr, 3))

max_now = 0
for i in list_all:
    j = int(n/i[0]) * int(m/i[1]) * int(l/i[2])
    max_now = max(max_now,j)

print(max_now)
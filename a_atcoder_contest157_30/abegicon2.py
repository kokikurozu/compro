xy=[list(map(int,input().split()))for _ in range(3)]
N = int(input())

for i in range(N):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if xy[j][k] == b:
                xy[j][k] = 0

Is_bingo = 0

sum_diagonal = 0
for m in range(3):
    sum_diagonal += xy[m][m]
if sum_diagonal == 0:
    Is_bingo = 1

sum_diagonal = 0
for n in range(3):
    sum_diagonal += xy[n][2-n]
if sum_diagonal == 0:
    Is_bingo = 1

for l in xy:
    if sum(l) == 0:
        Is_bingo = 1

tr = []
for o in range(3):
    tr_row = []
    for vector in xy:
        tr_row.append(vector[o])
    tr.append(tr_row)    

for l in tr:
    if sum(l) == 0:
        Is_bingo = 1

if Is_bingo == 1:
    print('Yes')
else:
    print('No')
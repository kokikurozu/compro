n,m = map(int,input().split())
#listA=[] #appendのために宣言が必要
list_rank = [[0,i] for i in range(2*n)]
listA = [input() for i in range(2*n)]
def judge(a,b):
    if a == b:
        return 0
    if a == 'G' and b =='C': 
        return 1
    if a == 'C' and b =='P': 
        return 1
    if a == 'P' and b =='G': 
        return 1
    return 2

for i in range(m):
    for j in range(n):
        a_rank = list_rank[2*j][1]
        b_rank = list_rank[2*j+1][1]
        winner = judge(listA[a_rank][i],listA[b_rank][i])
        if winner != -1:
            list_rank[2*j + winner - 1][0] -= 1
    list_rank.sort()

for i in range(2*n):
    print(list_rank[i][1] + 1)
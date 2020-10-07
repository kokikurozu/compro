N, M = map(int, input().split())
listA = list(map(int, input().split()))
listA.sort()

cnt = 0

yukohyo = sum(listA)/(4*M)

for i in listA:
    if i >= yukohyo:
        cnt += 1

if cnt >= M:
    print('Yes')
else:
    print('No')
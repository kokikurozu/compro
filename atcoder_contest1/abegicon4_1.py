N = int(input())
li = list(map(int, input().split()))
for i in range(len(li)):
    goukei = 0
    x = li[i]
    del li[i]
#    print(li)
    for j in range(N):
        goukei += li.count(j) * (li.count(j)-1) / 2
    print(int(goukei))
    li.insert(i, x)

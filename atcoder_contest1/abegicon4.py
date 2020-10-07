N = int(input())
li = list(map(int, input().split()))
j1=0
#print(li)
li.sort()
#print(li)
for i in range(len(li)):
    goukei = 0
    x = li[i]
    del li[i]
    #print(li)
    for j in li:
        if j != j1:
            goukei += li.count(j) * (li.count(j)-1) / 2
        j1 = j
    li.insert(i, x)
    print(int(goukei))

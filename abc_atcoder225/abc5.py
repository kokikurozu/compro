n,q = map(int,input().split())
li = [-1 for i in range(n+1)]
s = [list(map(int, input().split())) for _ in range(q)]

for i in range(q):
    count = 0
    z = [0 for i in range(n)]
    if s[i][0] == 1:
        li[s[i][1]] = s[i][2]
    elif s[i][0] == 2:
        li[s[i][1]] = -1
    else:
        x = s[i][1]
        while True:
            try:
                x = li.index(x)
            except:
                break
        for i in range(n):
            if x < 0:
                break
            z[i] = x
            x = li[x]
            count += 1
        print(count, end = ' ')
        for i in range(0,q):
            if z[i+1] == 0:
                print(z[i])
                break
            print(z[i],end = ' ')
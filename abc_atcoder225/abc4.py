n,q = map(int,input().split())
li = [-1 for i in range(n+1)]
s = [list(map(int, input().split())) for _ in range(q)]
 
def back_search(a):
    a.index()
    return
 
def front_search(a):
    return
 
for i in range(q):
    z = []
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
        while True:
            if x < 0:
                break
            z.append(x)
            x = li[x]
        print(len(z), end = ' ')
        for i in range(len(z)-1):
            print(z[i],end = ' ')
        print(z[-1])
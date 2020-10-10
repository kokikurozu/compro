def fact(A): #fact(int)
    c0 = A
    r = 2
    lis = []
    count = 1
    while A != 1:
        if A%r == 0:
            A = A//r
            lis.append(r)
            r = 2
        else:
            r += 1
        if r > int(pow(c0,0.5))+1:
            lis.append(A)
            break
    return(lis)


n = int(input())
lis = fact(n)
if n == 2 or len(lis) == 1:
    print("impossible")
elif n%2 == 0:
    print(n//2)
    for i in range(n//2):
        print(2, n-1-2*i, n+1+2*i)
    
else:
    p = lis[0] #pは素因数分解の最小数
    g = [[] for i in range(p)]
    s = [0]*p #3つ分箱を作っているだけ
    
    a = [1+2*i for i in range(n)] #今回分割する対象になるリスト
    
    for i in range(n//p-1):#切り捨て除算
        for j in range(p):
            s[j] += a[i*p + (j + i)%p]
            g[j].append(a[i*p + (j + i)%p])
    
    t = [ [i,s[i]] for i in range(p)]
    t.sort(key= lambda val : val[1], reverse=True)
    b = a[n-p:]
    
    for i in range(p):
        t[i][1] += b[i]
    
    for i in range(p):
        g[t[i][0]].append(b[i])

    print(p)
    
    #以下は書き出す処理
    for i in range(p):
        print(n//p,end="")
        print(" ",end="")
        
        for j in range(n//p):
            
            print(g[i][j],end="")
            if j != n//p-1:
                print(" ",end="")
        print()
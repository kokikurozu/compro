def main():
    n=int(input())
    tree=[tuple(map(int,input().split())) for _ in range(n)]
    TREE=set(tree)
    print(tree)
    ans=0
    for i in range(n-1):
        a,b=tree[i]
        for k in range(i+1,n):
            c,d=tree[k]
            x=c-a
            y=b-d
            if (a+y,b+x) in TREE and (c+y,d+x) in TREE:
                S=x**2+y**2
                if S>ans:
                    ans=S
            elif (a-y,b-x) in TREE and (c-y,d-x) in TREE:
                S=x**2+y**2
                if S>ans:
                    ans=S
    print(ans)
main()
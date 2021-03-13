from heapq import*
N,M=map(int,input().split())
abc=[list(map(int,input().split()))for _ in range(M)]
 
G=[[]for _ in range(N+1)]
for a,b,c in abc:
    G[a].append((c,b))
 
for i in range(1,N+1):
    que=[]
    dist=[10**9]*(N+1)
    for c,x in G[i]:
        heappush(que,(c,x))
    while que:
        c,x=heappop(que)
        if c<dist[x]:
            dist[x]=c
            for nc,nx in G[x]:
                heappush(que,(nc+c,nx))
    ans=dist[i]
    if ans==10**9:
        ans=-1
    print(ans)
i,N,K=map(int,input().split())
S=[list(input())for _ in range(N)]

from collections import*
from copy import *

sx=int(N//2)
sy=int(N//2)

Q=0
ans=[]
while 1:
    Q+=1
    C=defaultdict(int)
    que=deque([[sx,sy]])
    dist=[[10000]*N for _ in range(N)]
    dist[sy][sx]=0
    A=S[sy][sx]
    while que:
        x,y=que.popleft()
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx=x+dx
            ny=y+dy
            if 0<=nx<N and 0<=ny<N:
                if S[ny][nx]==A and dist[ny][nx]>dist[y][x]+1:
                    que.append([nx,ny])
                    dist[ny][nx]=dist[y][x]+1
                elif S[ny][nx]!=A:
                    C[S[ny][nx]]+=1
    A=max(C, key=C.get)
    ans.append([sy+1,sx+1,A])
    B=S[sy][sx]
    que=deque([[sx,sy]])
    dist=[[10000]*N for _ in range(N)]
    dist[sy][sx]=0
    while que:
        x,y=que.popleft()
        S[y][x]=A
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx=x+dx
            ny=y+dy
            if 0<=nx<N and 0<=ny<N:
                if S[ny][nx]==B and dist[ny][nx]>dist[y][x]+1:
                    que.append([nx,ny])
                    dist[ny][nx]=dist[y][x]+1
    if all(len(set(s))==1 for s in S):
        break

print(Q)
for y,x,c in ans:
    print(y,x,c)
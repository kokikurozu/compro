from bisect import *

n,q = map(int,input().split())
Ai = list(map(int,input().split()))
Ai.sort()

for i in range(q):
    x = int(input())
    print(len(Ai) - bisect_left(Ai,x))
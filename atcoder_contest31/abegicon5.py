'''N = int(input())
xy=[list(map(int,input().split()))for _ in range(N)]
'''
#マンハッタン距離
n = int(input())
x = [0]*n
for i in range(n):
    x[i] = list(map(int,input().split()))

d0 = [0]*n
d1 = [0]*n
for i,[x,y] in enumerate(x) :
    d0[i] = x-y
    d1[i] = x+y

print(max(max(d0)-min(d0), max(d1)-min(d1)))

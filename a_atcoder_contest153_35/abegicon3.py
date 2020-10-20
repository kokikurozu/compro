N,K = map(int,input().split())
H = list(map(int,input().split()))

H.sort(reverse=True)
try:
    for i in range(K):
        H[i] = 0
except:
    pass

print(sum(H))
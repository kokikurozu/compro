N = int(input())
ai = list(map(int,input().split()))
xor = 0
bi = []
for i in range(N):
    xor=xor^ai[i]
for j in range(N):
    bi.append(xor^ai[j])

for i in range(len(bi)-1):
    print(bi[i],end=' ')
print(bi[len(bi)-1])
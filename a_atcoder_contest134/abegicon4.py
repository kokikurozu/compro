N = int(input())
ai = (list(map(int,input().split())))
ai.insert(0,0)
hako = [0 for _ in range(N+1)]
hako_no = [0 for _ in range(N+1)]

for i in range(N, int(N/2), -1):
    hako[i] = ai[i]
for i in range(int(N/2), 0 ,-1):
    gokei = 0
    for j in range(i,N,i):
        gokei += hako[j]
    if gokei % 2 != ai[i]:
        hako[i] = 1
        hako_no[i] = i

hako_no.sort(reverse=True)
x = sum(hako_no)
print(x)
if x != 0: 
    print(*hako_no[0:x])
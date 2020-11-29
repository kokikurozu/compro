N = int(input())
ai = list(map(int,input().split()))
gokei = sum(ai)
min_now = float('inf')
cnt = 0

for i in range(N-1):
    cnt += ai[i]
    min_now = min(abs(gokei-2*cnt),min_now)
print(min_now)
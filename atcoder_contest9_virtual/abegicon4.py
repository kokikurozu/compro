N, x = map(int, input().split())
ai = list(map(int, input().split()))
gokei = 0
if ai[0] > x:
    gokei += ai[0] - x
    ai[0] = ai[0] - (ai[0] - x)

for i in range(N - 1):
    taberu = ai[i] + ai[i+1] - x
    if taberu > 0:
        gokei += taberu
        ai[i+1] = ai[i+1] - taberu 
print(gokei)
       
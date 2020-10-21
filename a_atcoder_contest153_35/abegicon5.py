H,N = map(int, input().split())
AB=[list(map(int,input().split()))for _ in range(N)]
cospa = []
for a,b in AB:
    cospa.append(a / b)
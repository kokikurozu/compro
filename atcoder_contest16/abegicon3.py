X, N = map(int, input().split())
pi = list(map(int, input().split()))
newpi = [0 for i in range(N)]
for i in range(N):
    newpi[i] = pi[i] - X
for x in range(101):
    if not(((-1) * x) in newpi):
        print((-1) * x + X)
        break
    if not(x in newpi):
        print(x + X)
        break
    
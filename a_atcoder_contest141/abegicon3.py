N, K, Q = map(int,input().split())

need = Q - K
players = [0 for _ in range(N)]

for i in range(Q):
    players[int(input()) - 1] += 1

for i in players:
    if i > need:
        print('Yes')
    else:
        print('No')
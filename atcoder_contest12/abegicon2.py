K = int(input())
S = str(input())
mojiretu = ''
if len(S) <= K:
    print(S)
else:
    S = list(S)
    for i in range(K):
        mojiretu += S[i]
    mojiretu += "..."
    print(mojiretu)
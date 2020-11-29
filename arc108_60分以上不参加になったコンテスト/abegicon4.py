N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = list(str(input()))
score = 0
use_K = [0] * K
use_K_flag = K

for i in range(len(T)):
    if T[i] == 'r':
        get = P
    if T[i] == 's':
        get = R
    if T[i] == 'p':
        get = S
    if i >= K:
        if T[i-K] == T[i]:
            T[i] = 0
            get = 0
    score += get

print(score)
#rの時はP点、sの時はR点、pの時はS点
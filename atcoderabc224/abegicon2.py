S = str(input())
max_S = S
min_S = S
for i in range(len(S)+1):
    S = S + S[0]
    S = S[1:]
    max_S = max(max_S,S)
    min_S = min(min_S,S)
print(min_S)
print(max_S)
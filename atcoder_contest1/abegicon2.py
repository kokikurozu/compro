S = str(input())
judge = 'Yes'
S = list(S)
for i in range(int(len(S)/2)):
    if S[i] != S[len(S) - 1 - i]:
        judge = 'No'
for i in range(int(len(S)/4)):
    if S[i] != S[int(len(S)/2) - 1 - i]:
        judge = 'No'
for i in range(int(len(S)/4)):
    if S[i + int(len(S)/2) + 1] != S[int(len(S)) - 1 - i]:
        judge = 'No'
print(judge)
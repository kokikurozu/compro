from collections import Counter

S = list(input())
Is_judge = 'No'
S.sort()

x = Counter(S)
for i in range(1,10,1):
    if not(i in x):
        x[i] = 0

if len(S) == 1:
    if S[0] == '8':
        Is_judge = 'Yes'

elif len(S) == 2:
    if int(S[0] + S[1]) % 8 == 0 or int(S[1] + S[0]) % 8 == 0:
        Is_judge = 'Yes'

else:
    for i in range(104, 1000+1, 8):
        now_judge = 1
        y = Counter(list(str(i)))
        for j in y:
            if y[j] > x[j]:
                now_judge = 0
                break
        if now_judge == 1:
            Is_judge = 'Yes'
            break

print(Is_judge)
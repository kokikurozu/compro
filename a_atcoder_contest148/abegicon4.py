N = int(input())
ai = list(map(int,input().split()))
i = 1
for j in ai:
    if j == i:
        i += 1
if i == 1:
    print(-1)
else:
    print(len(ai) - (i - 1))
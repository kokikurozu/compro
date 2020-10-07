N = int(input())
Ai = list(map(int, input().split()))
if N % 2 == 0:
    leftAi = Ai[:int(N/2)]
    rightAi = Ai[int(N/2):]
else:
    leftAi = Ai[:int(N/2)]
    rightAi = Ai[int(N/2 + 1):]
    middle = Ai[int(N/2)]
print(leftAi)
print(rightAi)

leftAi.sort()
rightAi.sort(reverse=True)
newAi = leftAi.extend(rightAi)
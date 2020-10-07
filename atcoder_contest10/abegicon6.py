X = []
a = -1
cnt = 0
N = int(input())
while N > 0:
    N -= 1
    X.append(int(input()))

X.sort()
for di in X:
    if di != a:
        cnt += 1
    a = di

print(cnt)
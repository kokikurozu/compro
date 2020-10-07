N = int(input())
S = str(input())
countRGB = S.count("RGB")
S = list(S)
x = 0
y = 0
z = 0
cnt = 0

for i in S:
    x += 1
    newS = S[x:]
    y = 0
    for j in newS:
        y += 1
        if j == "G":
            newnewS = newS[y:]
            cnt += newnewS.count("B")
print(cnt - countRGB)

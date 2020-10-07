N = int(input())
S = str(input())
countRGB = S.count("R.*G.*B")
S = list(S)
x = 0
y = 0
z = 0
cnt = 0



for i in S:
    setRGB = set("RGB")
    x += 1
    newS = S[x:]
    y = 0
    newsetRGB = setRGB - set(i)
    for j in newS:
        y += 1
        setRGB = newsetRGB
        if j != i:
            newnewsetRGB = newsetRGB - set(j)
            newnewS = newS[y:]
            listA = list(newnewsetRGB)
            cnt += newnewS.count(listA[0])
print(cnt - countRGB)

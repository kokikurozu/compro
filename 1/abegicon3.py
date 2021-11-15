n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
sen = [s[i][0]/s[i][1] for i in range(n)]
x = sum(sen)
point = 0
pos = 0
for i in range(len(sen)):
    point += sen[i]
    pos += s[i][0]
    if point >= x/2:
        point -= sen[i]
        pos -= s[i][0]
        break
y = (x/2) - point
z = (y * s[i][1])
pos += z
print(pos)
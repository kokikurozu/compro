N = int(input())
*listW,=input().split()
#listW = list(map(str, input().split()))
nengo = []
cnt = 0

for i in listW:
    x = list(i)
    nengo = []
    for j in x:
        if j == 'b' or j == 'c' or j == 'B' or j == 'C':
            nengo.append(1)
        elif j == 't' or j == 'j' or j == 'T' or j == 'J':
            nengo.append(3)
        elif j == 'l' or j == 'v' or j == 'L' or j == 'V':
            nengo.append(5)
        elif j == 'p' or j == 'm' or j == 'P' or j == 'M':
            nengo.append(7)
        elif j == 'n' or j == 'g' or j == 'N' or j == 'G':
            nengo.append(9)
        elif j == 'd' or j == 'w' or j == 'D' or j == 'W':
            nengo.append(2)
        elif j == 'f' or j == 'q' or j == 'F' or j == 'Q':
            nengo.append(4)
        elif j == 's' or j == 'x' or j == 'S' or j == 'X':
            nengo.append(6)
        elif j == 'h' or j == 'k' or j == 'H' or j == 'K':
            nengo.append(8)
        elif j == 'z' or j == 'r' or j == 'Z' or j == 'R':
            nengo.append(0)
        else:
            kiwqd = 0
        listW[cnt] = nengo
    cnt += 1

mojiretsu = ''
for k in listW:
    if k != []:
        if mojiretsu != '' and l != 200:
            mojiretsu = mojiretsu + ' '
        l = 200
        for l in k:
            mojiretsu = mojiretsu + str(l)
print(mojiretsu)
        
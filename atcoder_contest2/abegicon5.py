X, Y, A, B, C = map(int,input().split())
listp = list(map(int, input().split()))
listq = list(map(int, input().split()))
listr = list(map(int, input().split()))

listp = sorted(listp, reverse=True)
listq = sorted(listq, reverse=True)
listr = sorted(listr, reverse=True)
listp = listp[:X]
listq = listq[:Y]
listr = listr[:X+Y]
listp.insert(0, 1000000000000)
listq.insert(0, 1000000000000)


eat_noapple = []
oisisa = 0

for noapple in listr:
    if listp[-1] >= listq[-1] and listq[-1] < noapple:
        listq.pop(-1)
        eat_noapple.append(noapple)
    elif listp[-1] < listq[-1] and listp[-1] < noapple:
        listp.pop(-1)
        eat_noapple.append(noapple)
    else:
        break
listp.pop(0)
listq.pop(0)

try:
    for papple in listq:
        oisisa += papple
except:
    a = 0
try:
    for qapple in listp:
        oisisa += qapple
except:
    a = 0
try:
    for rapple in eat_noapple:
        oisisa += rapple
except:
    a = 0
print(oisisa)
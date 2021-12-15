x = float(input())
strx = str(x)
z = strx[len(str((int(x))))+1]
if int(z) >= 5:
    print(int(x)+1)
else:
    print(int(x))
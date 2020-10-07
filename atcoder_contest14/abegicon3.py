A, B = map(str, input().split())
A = str(A)
lenA = len(A)
A = int(A)
listB = list(B)
cnt = 0
j = 0
for i in listB:
    try:
        x = A * int(i) / (10**j)
        cnt += x
        j += 1
    except:
        None
cntx = int(cnt)
print(cntx)
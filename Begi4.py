judge = False
N = int(input())
for i in range(9):
    for j in range(9):
        #print((i+1) * (j+1))
        if (i+1) * (j+1) == N:
            judge = True

if judge == True:
    print('Yes')
else:
    print('No')
 
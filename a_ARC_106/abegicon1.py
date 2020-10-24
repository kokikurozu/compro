N = int(input())
Is_judge = 0
for A in range(1,40,1):
    for B in range(1,29,1):
        if (3 ** A + 5 ** B) == N:
            Is_judge = 1
            break
    else:
        continue
    break

if Is_judge == 0:
    print(-1)
else:
    print(A,B)
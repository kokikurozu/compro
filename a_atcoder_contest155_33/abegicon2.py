N = int(input())
A = list(map(int,input().split()))
IS_judge = 1
for i in A:
    if i % 2 == 0:
        if i % 3 == 0 or i % 5 == 0:
            pass
        else:
            IS_judge = 0
            break

if IS_judge == 1:
    print('APPROVED')
else:
    print('DENIED')

K = int(input())
A, B = map(int,input().split())

IS_judge = 0
for i in range(1000):
    if A <= K*i <= B:
        IS_judge = 1
        break
if IS_judge == 0:
    print('NG')
else:
    print('OK')
judge = True
N = int(input())
while True:
    try:
        listA=list(map(int,input().split()))
        if ((listA[1] + listA[2]) % 2 != listA[0] % 2) or (listA[0] < (listA[1] + listA[2])):
            judge = False
            print('No')
            break
    except:
        break

if judge == True:
    print('Yes')
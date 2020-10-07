N, M = map(int, input().split())
heyaA = list(map(int, input().split()))
kyakuB = list(map(int, input().split()))
cnt = 0

heyaA.sort(reverse=True)
kyakuB.sort(reverse=True)
judge = 1

if M > N:
    print('NO')#予約のほうが多い

else:
    for i in kyakuB:
        if i > heyaA[cnt]:
            judge = 0
        cnt += 1
    if judge == 0:
        print('NO')
    else:
        print('YES')
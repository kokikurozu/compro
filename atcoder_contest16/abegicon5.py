from itertools import permutations

N, M = map(int, input().split())
count = 0
all_denkyu_list = []

for i in range(M):
    listdenkyu = list(map(int, input().split()))
    denkyu = [0 for i in range(N)]
    now_denkyu = denkyu
    for j in range(1, len(listdenkyu)):
        now_denkyu[listdenkyu[j] - 1] = 1
    all_denkyu_list.append(now_denkyu)

amari_denkyu_list = list(map(int, input().split()))
switch_ONOFF_list = permutations([0, 1], N)
x = -1


for k in switch_ONOFF_list:
    is_judge = 1
    x += 1
    for l in all_denkyu_list:
        cnt = 0
        for m in range(N):
            cnt += k[m] * l[m]
        if cnt % 2 != amari_denkyu_list[x]:
            is_judge = 0
            break
    if is_judge == 1:
        count += 1
print(count)
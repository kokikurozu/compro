H,W = map(int,input().split())

string_list=[input() for i in range(H)]

cnt = 0
new_list = []

for j in string_list:
    Is_cnt = 0
    list_j = list(j)
    new_list.append(list_j)
    for pointj in list_j:
        if pointj == '.':
            Is_cnt += 1
            if Is_cnt >= 2:
                cnt += 1
        else:
            Is_cnt = 0

for k in range(W):
    Is_cnt = 0
    for l in range(H):
        if new_list[l][k] == '.':
            Is_cnt += 1
            if Is_cnt >= 2:
                cnt += 1
        else:
            Is_cnt = 0

print(cnt)

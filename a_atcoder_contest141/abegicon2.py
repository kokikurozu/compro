S = input()
flag = [1,1]
cnt = 0
for i in S:
    cnt += 1
    if cnt % 2 == 1:
        if i == 'L':
            flag[0] = 0
    if cnt % 2 == 0:
        if i == 'R':
            flag[1] = 0

if sum(flag) >= 2:
    print('Yes')
else:
    print('No')
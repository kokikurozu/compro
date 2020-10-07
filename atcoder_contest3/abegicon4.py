K = list(str(input()))
cnt = 9
all_cnt = 9
count = 1
ans = 0
for i in range(len(K)-1):
    cnt = cnt * 3 - 3 ** i


K.reverse()

for j in K:
    count += 1
    if count == 1:
        ans += int(K)
    elif count == 2:
        ans += int()

N = int(input())
D = [list(input().split()) for _ in range(N)] #_それ自体に意味はないということ
cnt = 0
IS_cnt = "No"
for i in D:
    if i[0] == i[1]:
        cnt += 1
        if cnt == 3:
            IS_cnt = "Yes"
            break
    else:
        cnt = 0
print(IS_cnt)

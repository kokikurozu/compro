n,x = map(int,input().split())

s = [list(map(int, input().split())) for _ in range(n)]
soseki = 1
ans = 0
s_count = [0 for i in range(n)]
for i in range(n):
    soseki *= (len(s[i])-1)
    s_count[i] = len(s[i]) - 1
s_counter = [1 for i in range(n)]
for k in range(soseki):
    seki = 1
    for i in range(0,n):
        seki *= s[i][s_counter[i]]
    if seki == x:
        ans += 1
    flg = n-1
    while True:
        s_counter[flg] += 1
        if s_counter[flg] > s_count[flg]:
            s_counter[flg] = 1
            flg -= 1
        else:
            break
    if s_counter[0] > s_count[0]:
        break
print(ans)


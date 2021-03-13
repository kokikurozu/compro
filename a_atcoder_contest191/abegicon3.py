h,w = map(int,input().split())
s = [list(input()) for i in range(h)]
ans = 0
for i in range(h-1):
    for j in range(w-1):
        cnt = 0
        if s[i][j] == '#':
            cnt += 1
        if s[i+1][j] == '#':
            cnt += 1
        if s[i][j+1] == '#':
            cnt += 1
        if s[i+1][j+1] == '#':
            cnt += 1
        if cnt % 2 == 1:
            ans += 1
print(ans)
n,m = map(int,input().split())
s = [list(map(int, input().split())) for _ in range(n)]
flg = 'Yes'
for i in range(n):
    for j in range(m-1):
        if (((s[i][j] - 1) % 7) + 1 == (s[i][j+1] - 1) % 7) and (s[i][j] + 1) == s[i][j+1]:
            flg = 'Yes'
        else:
            flg = 'No'
            break
for i in range(n-1):
    if s[i][0] + 7 != s[i+1][0]:
        flg = 'No'
        break
print(flg)
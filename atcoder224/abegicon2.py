h,w = map(int,input().split())
s = [list(map(int, input().split())) for _ in range(h)]
flg = 'Yes'

for i1 in range(h):
    for i2 in range(i1,h):
        for j1 in range(w):
            for j2 in range(j1,w):
                if s[i1][j1] + s[i2][j2] > s[i2][j1] + s[i1][j2]:
                    flg = 'No'
                    break

print(flg)
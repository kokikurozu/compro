xy=[list(map(int,input().split()))for _ in range(4)]
ans = 'GAMEOVER'
for i in range(4):
    for j in range(4):
        if i > 0:
            if xy[i][j] == xy[i-1][j]:
                ans = 'CONTINUE'
        if i < 3:
            if xy[i][j] == xy[i+1][j]:
                ans = 'CONTINUE'
        if j > 0:
            if xy[i][j] == xy[i][j-1]:
                ans = 'CONTINUE'
        if j < 3:
            if xy[i][j] == xy[i][j+1]:
                ans = 'CONTINUE'
        
print(ans)
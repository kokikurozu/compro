from collections import deque

def f(x1,y1,x2,y2,q_num):
    if 0 <= x2 <= n-1 and 0 <= y2 <= n-1:
        if group[x2][y2] == 0 and s[x2][y2] == q_num:
            print(i,j,s[x2][y2] == q_num,s[x2][y2],q_num)

            group[x2][y2] = group[x1][y1]
            q.append([x2,y2])

_, n, k = map(int,input().split())

s = [list(map(int,list(input()))) for _ in range(n)]
group = [[0 for j in range(n)] for i in range(n)]

x = 1
for i in range(n):
    for j in range(n):
        if group[i][j] == 0:
            q = deque([])
            q.append([i,j])
            group[i][j] = x
            x += 1
            
            q_num = s[i][j]
            
            while q:
                [x0,y0] = q.popleft()

                # 4方向の数字を確認する
                # 数字がq_numと等しいならqに追加する
                
                f(x0,y0,x-1,y0,q_num)
                f(x0,y0,x+1,y0,q_num)
                f(x0,y0,x,y0+1,q_num)
                f(x0,y0,x,y0-1,q_num)
for i in range(n):
    print(group[i])
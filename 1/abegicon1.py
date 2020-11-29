h,w = map(int,input().split())
new_list = [['#' for j in range(w)] for i in range(h)]
#new_list = [[] for i in range(h)]
xy = []
for i in range(h):
    xy.append(input())
for i in range(h):
    for j in range(w):
        cnt = 0
        if xy[i][j] == '#':
            new_list[i][j] = '#'
        else:
            if xy[i][j-1] == '#' and j-1 >= 0:
                cnt += 1
            try:
                if xy[i+1][j] == '#' and i+1 <= h:
                    cnt += 1
            except:
                pass
            if xy[i-1][j] == '#' and i-1 >= 0:
                cnt += 1
            try:
                if xy[i][j+1] == '#' and j+1 <= w:
                    cnt += 1
            except:
                pass
            if xy[i-1][j-1] == '#' and j-1 >= 0 and i-1 >= 0:
                cnt += 1
            try:
                if xy[i+1][j-1] == '#' and i+1 <= h and j-1 >= 0:
                    cnt += 1
            except:
                pass
            try:
                if xy[i-1][j+1] == '#' and i-1 >= 0 and j+1 <= w:
                    cnt += 1
            except:
                pass
            try:
                if xy[i+1][j+1] == '#' and j+1 <= w and i+1 <= h:
                    cnt += 1
            except:
                pass
            
            new_list[i][j] = cnt

for k in new_list:
    for j in k:
        print(j,end='')
    print()
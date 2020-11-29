#dxを使って解く
#dxは迷路系の問題で、周囲を検索するなどで使用できる
#ここではrange(-1,2)とすることで、-1,0,1をdxとして指定している
h,w = map(int,input().split())
list_s = [list(input()) for i in range(h)]
new_list = [[0 for _ in range(w)] for _ in range(h)]
for a in range(h):
    for b in range(w):
        cnt = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if a+i < h and b+j < w and a+i >= 0 and b+j >= 0:
                    if i != 0 or j != 0:
                        if list_s[a+i][b+j] == '#':
                            cnt += 1
        if list_s[a][b] == '#':
            cnt = '#'
        print(cnt,end='')
    print()

#ようは地図に対して使う全探索
import sys
sys.setrecursionlimit(500000)

h,w = map(int,input().split())
xy = [list(input()) for i in range(h)]
check = [[0] * w for i in range(h)] #区画を調べたか保存する

def dfs(i,j):#深さ優先探索のこと
    if h<i+1 or i<0 or w<j+1 or j<0 or check[i][j] == 1 or xy[i][j]=='#':
        return
    elif xy[i][j]=='g':
        print('Yes')
        sys.exit(0)#プログラムを強制終了させる
        '''
        breakとして、is_flgを使うより簡単
        '''
    else:
        check[i][j] = 1
        dfs(i+1,j) #再帰的に自分自身を呼び出す
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)

#開始位置を探す
for i in range(h):
    for j in range(w):
        if xy[i][j] == 's':
            dfs(i,j)

print('No')
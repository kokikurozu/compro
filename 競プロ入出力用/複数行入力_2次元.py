n=3#縦の次元
#xy = [list(map(int,input().split())) for _ in range(n)]

f = [[0,0]] + [list(map(int,input().split())) for _ in range(n)] #0から初めて混乱を避ける
ai = [0] + list(k for i in range(9)) #1行の場合
sp = [list(map(str,input().split()))+[i]for i in range(n)]#通し番号を付けたい場合

'''
1 4
3 7
2 6
'''
#print(xy)
print(f)
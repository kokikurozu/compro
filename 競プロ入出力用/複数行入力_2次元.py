n=3#縦の次元
xy = [list(map(int,input().split())) for _ in range(n)]

f = [[0,0] + list(map(int,input().split())) for _ in range(n)] #0から初めて混乱を避ける
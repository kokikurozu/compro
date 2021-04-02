from collections import deque
n = int(input())
xy = [[0,0]] + [list(map(int,input().split())) for _ in range(n-1)] #0から初めて混乱を避ける
q1 = deque(xy)
print(q1)
#def search_dist():
#   while q1:

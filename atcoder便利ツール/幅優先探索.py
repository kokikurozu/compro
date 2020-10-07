from collections import deque

r,c = map(int,input().split())
sy, sx = map(int,input().split())
gy, gx = map(int,input().split())
C = [0]*r

for i in range(r):
    C[i] = list(input())

reach = [[10**5 for i in range(c)] for j in range(r)]

reach[sy-1][sx-1] = 0
q1 = deque([sy-1])
q2 = deque([sx-1])

while q1:
    p1 = q1.popleft()
    p2 = q2.popleft()

    if C[p1-1][p2] == '.' and (reach[p1-1][p2] > reach[p1][p2] + 1):
        reach[p1-1][p2] = reach[p1][p2] + 1
        q1.append(p1-1)
        q2.append(p2)

    if C[p1+1][p2] == '.' and (reach[p1+1][p2] > reach[p1][p2] + 1):
        reach[p1+1][p2] = reach[p1][p2] + 1
        q1.append(p1+1)
        q2.append(p2)

    if C[p1][p2-1] == '.' and (reach[p1][p2-1] > reach[p1][p2] + 1):
        reach[p1][p2-1] = reach[p1][p2] + 1
        q1.append(p1)
        q2.append(p2-1)
    
    if C[p1][p2+1] == '.' and (reach[p1][p2+1] > reach[p1][p2] + 1):
        reach[p1][p2+1] = reach[p1][p2] + 1
        q1.append(p1)
        q2.append(p2+1)

print(reach[gy-1][gx-1])
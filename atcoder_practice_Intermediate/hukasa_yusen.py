import sys
sys.setrecursionlimit(1000000)

H, W  = map(int, (input().split()))
mati = []
reached = [[0] * W for i in range(H)]
for i in range(H):
    mati.append(list(map(str, input())))

def search(x, y):
    if x < 0 or W <= x or y < 0 or H <= y:
        return
    elif reached[y][x] == 1:
        return
    elif mati[y][x] == '#':
        return
    else:
        reached[y][x] = 1
    search(x + 1, y)
    search(x - 1, y)
    search(x, y - 1)
    search(x, y + 1)

for y1 in range(H):
    for x1 in range(W):
        if mati[y1][x1] == "s":
            sx, sy = x1, y1
        if mati[y1][x1] == "g":
            gx, gy = x1, y1

search(sx, sy)

if reached[gy][gx] == True:
    print("Yes")
if reached[gy][gx] == False:
    print("No")


import itertools

x, y = map(int, input().split())
N = int(input())

lista = [0] * N

for i in range(N):
    lista[i] = list(map(int, input().split()))

def main(x0, y0, x1, y1, x2, y2):
    bunshi = abs((y2-y1)*x0-(x2-x1)*y0+x2*y1-y2*x1)
    bunbo = ((y2-y1)**2 + (x2-x1)**2) ** (1/2)
    return bunshi/bunbo

now_min = 1000000000000000
for j in range(N):
    now = main(x, y, lista[j-1][0], lista[j-1][1], lista[j][0], lista[j][1])
    now_min = min(now_min, now)
print(now_min)
N, K = map(int, input().split())
shinsu = 0

while N >= 1:
    N = N / K
    shinsu += 1

print(shinsu)

N, M = map(int, input().split())
#goukei = comb(N, 2, exact=True) + comb(M, 2, exact=True)
goukei = N * (N-1) / 2 + M * (M - 1) / 2
print(int(goukei))
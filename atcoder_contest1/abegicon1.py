from scipy.special import comb
N, M = map(int, input().split())
goukei = comb(N, 2, exact=True) + comb(M, 2, exact=True)
print(goukei)
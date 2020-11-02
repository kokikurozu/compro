from bisect import *
N, K = map(int,input().split())
hi = list(map(int,input().split()))

hi.sort()

print(len(hi) - (bisect_left(hi, K)))
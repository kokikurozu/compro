N, R = map(int,input().split())
rate = 0
if N <= 10:
    rate = R + 100 * (10 - N)
else:
    rate = R
print(rate)
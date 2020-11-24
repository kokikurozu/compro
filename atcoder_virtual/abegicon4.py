n,m = map(int,input().split())

ans = (m * 1900 + 100 * (n-m)) * (2 ** m)
print(ans)
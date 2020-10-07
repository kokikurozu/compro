N , M = map(int, input().split())
listA=[int(input()) for i in range(N)]


def LIS(L, X):
  res=0
  N = len(L)
  dp=[1]*N
  for i in range(N):
    for j in range(i):
      if abs(L[j]-L[i]) <= X:
        dp[i]=max(dp[i],dp[j]+1)
    res=max(res,dp[i])
  return res

print(LIS(listA, M))
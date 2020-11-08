#一旦パス

N, M = map(int,input().split())
Ai = list(map(int,input().split()))
x = len(Ai) - 1
Ai.sort()
for i in range(M):
    Ai[x] /= 2


print(sum(Ai))

#方針

'''
まずは商品をsort(降順)
割引券を使うたびに、割引された商品が今何番目に高い商品かチェック(logN)
割引券が尽きるまで繰り返す(N)
最後に足し算(N)
N + NlogN でできそう
'''
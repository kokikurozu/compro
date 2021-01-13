#https://atcoder.jp/contests/abc130/tasks/abc130_d 問題url

L = -1
R = 0
n, k = map(int,input().split())
ai = list(map(int,input().split()))
ans = 0
gokei = 0
while R<n:
    gokei += ai[R]
    if gokei >= k:
        ans += (n - R)
        while L<R:
            L += 1
            gokei -= ai[L]
            if gokei >= k:
                ans += (n-R)
            else:
                break
    R += 1

print(ans)
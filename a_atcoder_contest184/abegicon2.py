N, X = map(int,input().split())
S = list(input())
ans = X
for i in S:
    if i == 'o':
        ans += 1
    elif i == 'x':
        if ans >= 1:
            ans -= 1
print(ans)

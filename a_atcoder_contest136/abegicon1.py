a, b, c = map(int,input().split())

if b + c < a:
    ans = 0
else:
    ans = c - (a-b)
print(ans)
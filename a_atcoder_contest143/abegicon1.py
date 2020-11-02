A,B = map(int,input().split())

ans = A - 2 * B
if ans >= 0:
    print(ans)
else:
    print(0)
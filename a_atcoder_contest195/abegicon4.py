b,c = map(int,input().split())

if b <= 0:
    if c >= abs(b)*2:
        ans = c + abs(b)*2
    else:
        ans = c * 2
elif b > 0:
    if c >= abs(b)*2:
        if c-2 <= 0:
            ans = 1 + abs(b) * 2
        else:
            ans = abs(b)*2 + c - 1
    else:
        if c-2<=0:
            ans = 1 + c
        else:
            ans = 2 * c - 1

print(ans)
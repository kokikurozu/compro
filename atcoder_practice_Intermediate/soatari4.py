A, B, C, X, Y = map(int, input().split())

if X > Y:
    many = A
else:
    many = B
    

if min(A, B) > 2 * C:
    ans = C * 2 * max(X, Y)
elif (A + B) / 2 <= C:
    ans = A * X + B * Y
else:
    ans = min(X, Y) * 2 * C + (max(X, Y) - min(X, Y)) * many

print(ans)
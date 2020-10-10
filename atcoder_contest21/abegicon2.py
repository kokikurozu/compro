a, b, c, d = map(int, input().split())
if a <= c <= b <= d or c <= a <= d <= b or a <= c <= d <= b or c <= a <= b <= d:
    print("Yes")
else:
    print("No")
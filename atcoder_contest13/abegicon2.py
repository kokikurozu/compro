x1, y1, x2, y2, x3, y3 = map(int, open(0).read().split())
ans = 0.5 * ((x1-x3) * (y2-y3) - (x2-x3) * (y1 - y3))
print(abs(ans))
import math
A, B, H, M = map(int,open(0).read().split())
jishin = 30 * H + 0.5 * M
hunshin = M * 6
kakuAB = jishin - hunshin
kakuAB = math.radians(kakuAB)
C = abs(A**2 + B**2 - 2*A*B*math.cos(kakuAB)) ** 0.5
print(C)
import math

a, b, c, d = map(int,input().split())
kosu = b-a+1
x = (kosu/c) + (kosu/d) - (kosu/math.gcd(c,d))
ans = kosu - x
print(ans)
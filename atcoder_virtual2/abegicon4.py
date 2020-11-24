import math

x,y,a,b = map(int,input().split())
keikenti = 0
while x*a - x < b and x * a < y:
    x = x * a
    keikenti += 1

keikenti += ((y - 1 - x)//b)
print(keikenti)
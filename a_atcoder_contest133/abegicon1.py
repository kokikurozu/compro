n, a, b = map(int,input().split())
use_tax = a * n
if use_tax <= b:
    print(use_tax)
else:
    print(b)
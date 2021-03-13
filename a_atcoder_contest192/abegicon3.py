n,k = map(int,input().split())
for i in range(k):    
    x_small = int(''.join(sorted(str(n))))
    x_big = int(''.join(sorted(str(n),reverse = True)))
    n = x_big - x_small

print(n)
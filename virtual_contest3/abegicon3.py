k,a,b = map(int,input().split())
bis = 1
use_k = k
if a >= b-2:
    print(k+1)
else:
    use_k = use_k - (a - 1)
    bis = a
    bis += (b-a)*(use_k//2)
    if use_k % 2 == 1:
        bis += 1
    print(bis)
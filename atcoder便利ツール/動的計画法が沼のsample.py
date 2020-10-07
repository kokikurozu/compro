s = int(input())
mod = 10**9+7
d = [0]*(s+1)

for i in range(3,s+1):
    for j in range(3,s+1):
        
        if i-j < 3:
            break
        d[i] += d[i-j]
        d[i] %= mod
    d[i] += 1
    d[i] %= mod
        
print(d[-1]%mod)
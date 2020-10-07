import math

K = int(input())
count = 0
for i in range(1 ,K + 1 ,1):
    for j in range(1, K + 1, 1):
        for l in range(1 ,K + 1 ,1):
            count += math.gcd(math.gcd(i, j), l)
print(count)
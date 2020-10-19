N, k = map(int,input().split())
p = list(map(int,input().split()))
max_k = 0
for i in range(k):
    max_k += p[i]

new_k = max_k

for i in range(k, len(p), 1):
    new_k = new_k - p[i-k] + p[i]
    max_k = max(new_k, max_k)

print(max_k/2 + 0.5 * k)
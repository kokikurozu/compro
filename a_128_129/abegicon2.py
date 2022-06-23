n = int(input())
wi = list(map(int,input().split()))
a = sum(wi)
b = 0
min_ans = a
for i in range(len(wi)):
    b += wi[i]
    a -= wi[i]
    min_ans = min(min_ans,abs(a-b))

print(min_ans)
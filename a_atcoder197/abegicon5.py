n = int(input())
a = list(map(int,input().split()))
left_x = 0
right_x = 0
z = []
min_ans = 1000000000000000000000
for i in range(n-1):
    left_x = 0
    right_x = 0
    for k in range(i+1):
        left_x = left_x | a[k]
    for j in range(i+1,n,1):
        right_x = right_x | a[j]
    z.append(left_x)
    z.append(right_x)
for i in range(len(z)):
    xor = left_x ^ right_x
    min_ans = min(min_ans,xor)

print(min_ans)
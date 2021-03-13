x = str(input())
m = int(input())
z = sorted(list(x),reverse=True)
d = int(z[0])
print(d)
d_ans = d
k = len(x)
for i in range(100000,2,-1):
    d = d_ans
    for j in range(len(x)):
        d = d * i
        if d > m:
            break
    if d <= m:
        break

print(i-d_ans + 1)
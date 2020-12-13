L = int(input())
x = 1
for i in range(1, L-11, 1):
    x = int((x * (L-i)) / i)

print(x)
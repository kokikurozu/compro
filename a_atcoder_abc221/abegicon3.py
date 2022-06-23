N = list(input())
N.sort(reverse=True)
N = ''.join(N)


x = N[0]
y = N[1]

for i in range(2, len(N)):
    if int(x) >= int(y):
        y += N[i]
    else:
        x += N[i]

print(int(x) * int(y))
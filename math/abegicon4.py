mae_x = 1
ans = 0
for i in range(2019):
    x = 1-mae_x
    ans += (mae_x**2 + (x-1)**2)**0.5
    mae_x = x

x = 2
ans += (mae_x**2 + (x-1)**2)**0.5

print(ans)
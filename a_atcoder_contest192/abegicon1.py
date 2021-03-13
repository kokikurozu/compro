x = int(input())
for i in range(100000):
    if x < 100:
        break
    x -= 100

print(100 - x)
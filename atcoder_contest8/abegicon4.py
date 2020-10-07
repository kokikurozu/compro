S = str(input())
now = 0
ai = [0 for i in range(200000)]
for i in range(200000):
    ai[i] = (10^i) % 2019
print(ai)
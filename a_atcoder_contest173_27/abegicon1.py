N = int(input())
for i in range(11):
    if N > 1000:
        N -= 1000
print(1000 - N)
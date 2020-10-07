from math import sqrt

N = int(input())
count = 0
for i in range(int(sqrt(N)), 0, -1):
    if N % i == 0:
        smallA = i
        break

bigA = N / smallA

while True:
    bigA /= 10
    count += 1
    if bigA < 1:
        break
print(count)
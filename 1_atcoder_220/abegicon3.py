n = int(input())
ai = list(map(int,input().split()))
x = int(input())
ans = 0
sum_ai = sum(ai)
count = n * (x // sum_ai)
x -= (x // sum_ai) * sum_ai

for i in ai:
    if x < 0:
        break
    count += 1
    x -= i


print(count)
S = int(input())
sum_now = 1
before_number = 1
before3 = [1, 1, 1]
for i in range(6, S+1, 1):
    sum_now = sum_now + before3[i % 3]
    before3[i % 3] = sum_now
if S == 1 or S == 2:
    print(0)
else:
    ans = sum_now % (10 ** 9 + 7)
    print(ans)
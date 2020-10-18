N = int(input())
x = list(map(int,input().split()))
now_min = 10 ** 20
new_min = 0
for i in range(1,100,1):
    new_min = 0
    for j in range(len(x)):
        new_min += (x[j] - i) ** 2
    now_min = min(new_min,now_min)
print(now_min)
n, p = map(int,input().split())
li = list(map(int,input().split()))
count = 0
for i in li:
    if i < p:
        count += 1
print(count)
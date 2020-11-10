A,B = map(int,input().split())

ku = 1
cnt = 0
for i in range(30):
    if ku < B:
        ku += (A - 1)
        cnt += 1
print(cnt)
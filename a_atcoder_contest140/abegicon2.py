N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

cnt = -1
ans = 0
for a in A:
    ans += B[a-1]
    if cnt + 1 == a:
        ans += C[a-2]
    cnt = a
print(ans)
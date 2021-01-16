N = int(input())
ans = 0
for i in range(1,N+1,1):
    if list(str(i)).count('7') >= 1:
        ans += 1
    elif list(oct(i)).count('7') >= 1:
        ans += 1

print(N - ans)
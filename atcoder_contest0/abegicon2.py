a, b, c, d = map(int, input().split())
ans1 = a * c
ans2 = a * d
ans3 = b * c
ans4 = b * d

ans = max(ans1,ans2,ans3,ans4)
print(ans)
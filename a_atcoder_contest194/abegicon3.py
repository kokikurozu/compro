n = int(input())
len_n = len(str(n))
print(len_n)
ans = 0
if len_n <= 3:
    print(0)
if 6 >= len_n >= 4:
    ans = 0
    print(ans + (n-999))
if 9 >= len_n >= 7:
    ans += 999000
    print(ans + (n-999999)*2)
if 12 >= len_n >= 10:
    ans += 2 * 999000000
    print(ans + (n-999999999)*3)
if 15 >= len_n >= 13:
    ans += 3 * 999000000000
    print(ans + (n-999999999999)*4)
if len_n == 16:
    ans += 4 * 999000000000000 + 5
    print(ans)
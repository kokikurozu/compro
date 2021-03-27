s = list(input())
ans = 0
flg = 0
start_a = 0
end_z = 0
for i in range(len(s)):
    if flg == 0:
        if s[i] == 'A':
            start_a = i
            flg = 1
    if flg == 1:
        if s[i] == 'Z':
            end_z = i
print(end_z-start_a+1)
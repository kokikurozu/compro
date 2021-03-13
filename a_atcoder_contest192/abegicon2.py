s = list(input())
Is_flg = 'Yes'
for i in range(len(s)):
    if i % 2 == 0:
        if ord(s[i]) < 97 or ord(s[i]) > 122:
            Is_flg = 'No'
    else:
        if ord(s[i]) < 65 or ord(s[i]) > 90:
            Is_flg = 'No'

print(Is_flg)
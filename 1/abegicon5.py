s = list(str(input()))
words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
min_use = 1000
max_bunkatu = 0
cnt = 0
for j in words:
    max_bunkatu = 0
    cnt = 0
    for i in range(len(s)):
        cnt += 1
        if s[i] == j:
            cnt -= 1
            max_bunkatu = max(cnt,max_bunkatu)
            cnt = 0
        max_bunkatu = max(cnt,max_bunkatu)
    min_use = min(max_bunkatu,min_use)
print(min_use)
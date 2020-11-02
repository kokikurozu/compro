N = int(input())
S = list(input())
now_slime = ''
cnt = 0
for i in S:
    if now_slime == i:
        cnt += 1
    now_slime = i

print(len(S)-cnt)
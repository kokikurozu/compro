S = str(input())
T = str(input())
count = 0
max_count = 0

for i in range(len(S)-len(T)+1):
    nowS = S[i:i+len(T)]
    for j in range(len(T)):
        if nowS[j] == T[j]:
            count += 1
    max_count = max(max_count, count)
    count = 0
print(len(T) - max_count)
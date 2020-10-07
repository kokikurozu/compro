N = int(input())
ai = [0 for i in range(N)]
for j in range(N):
    ai[j] = str(input())
s_ai = set(ai)
print(len(s_ai))
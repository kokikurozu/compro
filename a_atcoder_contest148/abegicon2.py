N = int(input())
S,T = map(str,input().split())
new_word = ''
for i in range(N):
    new_word += S[i]
    new_word += T[i]
print(new_word)
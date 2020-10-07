N = int(input())
S = list(input())
R = S.count("R")
G = S.count("G")
B = S.count("B")
countRGB = R * G * B

for i in range(N):
    try:
        for j in range(N):
            if S[i] != S[i + j] and S[i] != S[i + 2 * j] and S[i+j] != S[i + 2 * j]:
                countRGB -= 1
    except:
        pass
print(countRGB)
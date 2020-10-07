goukei = 0

N = int(input()) * (-1)
Ai = list(map(int, input().split()))
number = [j for j in range(0, N, -1)]
new_ai = number + Ai
new_ai = [x + y for (x, y) in zip(Ai, number)]
print(new_ai)
for i in range(len(Ai)):
    goukei += new_ai.count(-(Ai[i] - i))
print(goukei)
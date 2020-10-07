goukei = 0

N = int(input()) * (-1)
Ai = list(map(int, input().split()))
array_Ai = np.array(Ai)
number = np.array([j for j in range(0, N, -1)])
number_1 = np.array([1 for k in range(-N)])
new_ai = number + array_Ai
for i in range(len(Ai)):
    goukei += np.count_nonzero(new_ai == (-Ai[i] - i))
print(goukei)
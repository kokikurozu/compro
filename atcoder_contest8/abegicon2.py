A, B, C, D = map(int, input().split())
for i in range(105):
    C -= B
    if C <= 0:
        print("Yes")
        break
    A -= D
    if A <= 0:
        print("No")
        break
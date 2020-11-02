N = int(input())
Ai = list(map(int,input().split()))

list_student = [0 for _ in range(N)]
for j in range(len(list_student)):
    list_student[Ai[j] - 1] = j + 1

print(*list_student)
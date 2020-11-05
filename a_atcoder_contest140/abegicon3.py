N = int(input())
Ai = list(map(int,input().split()))

list_student = [0 for _ in range(N)]
for j in Ai:
    x = Ai.find(j)
    list_student[j-1] = Ai.find(j) + 1

s = ''
for i in range(len(list_student) - 1):
    s += str(list_student[i]) + ' '
s += str(list_student[len(list_student) - 1])
print(s)
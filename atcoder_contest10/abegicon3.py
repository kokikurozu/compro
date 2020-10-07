N, M = map(int, input().split())
Hi = list(map(int, input().split()))
is_judge_list = [1 for i in range(N)]

for j in range(M):
    A, B = map(int, input().split())
    if Hi[A-1] > Hi[B-1]:
       is_judge_list[B-1] = 0 
    elif Hi[B-1] > Hi[A-1]:
        is_judge_list[A-1] = 0
    else:
        is_judge_list[A-1] = 0
        is_judge_list[B-1] = 0
print(is_judge_list.count(1))

N, M, K = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int,input().split()))
minutes = sum(A)
cnt = len(A)
roopA_count = len(A) - 1
roopB_count = 0
max_cnt = 0

while roopA_count >= 0 and not(roopB_count == len(B)):
    if minutes > K:
        minutes -= A[roopA_count]
        cnt -= 1
        roopA_count -= 1
    if minutes <= K:
        max_cnt = max(cnt, max_cnt)
        while roopB_count < len(B):
            minutes += B[roopB_count]
            cnt += 1
            roopB_count += 1
            if minutes <= K:
                max_cnt = max(cnt, max_cnt)
            else:
                break
print(max_cnt)
H,A = map(int, input().split())
cnt = 0
while True:
    H -= A
    cnt += 1
    if H <= 0:
       print(cnt)
       break 
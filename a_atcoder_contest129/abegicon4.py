n = int(input())
ab=[list(map(int,input().split()))for _ in range(n)]
get_vote = [0] * n
aoki_vote_sum = 0
for i in range(n):
    get_vote[i] = ab[i][0] * 2 + ab[i][1]
    aoki_vote_sum += ab[i][0]
get_vote.sort(reverse=True)
ans = 0
taka_vote_sum = 0
for i in get_vote:
    if taka_vote_sum > aoki_vote_sum:
        break
    taka_vote_sum += i
    ans += 1
print(ans)
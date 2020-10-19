import sys

file_input = sys.stdin

V, E = map(int, file_input.readline().split())

no_route = 15001

# (v-1) th vertex is excluded
dp = [[no_route] * (V - 1) for i in range(1 << (V - 1))]

adj = [[] for i in range(V)]

for line in file_input:
    s, t, d = map(int, line.split())
    if s == V - 1:
        # Record the distance from the (v-1) th vertex to the adjacent vertex
        dp[1 << t][t] = d
    else: 
        # Store distance from source, not target
        adj[t].append((s, d))

# DP
for b in range(1, 1 << (V - 1)):
    for i in range(V - 1):
        b_i = 1 << i
        if b & b_i:
            pre_bit = b ^ b_i
            dp_pre = dp[pre_bit]
            for s, d in adj[i]:
                pre_rec = dp_pre[s]
                if pre_rec != no_route:
                    dp[b][i] = min(dp[b][i], pre_rec + d)

ans = no_route

# A state where all vertices other than (v-1) have been visited.
dp_comp = dp[(1 << (V - 1)) - 1]

for s, d in adj[V - 1]:
    comp_rec = dp_comp[s]
    if comp_rec != no_route:
        ans = min(ans, comp_rec + d)

if ans == no_route:
    print(-1)
else:
    print(ans)
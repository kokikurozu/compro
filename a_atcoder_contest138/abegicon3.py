#deque practice
from collections import deque

N = int(input())
vi = list(map(int,input().split()))
dvi = deque(vi)

for i in range(N-1):
    vi.sort(reverse = True)
    x = vi.pop()
    y = vi.pop()
    vi.append((x+y)/2)

print(vi[0])
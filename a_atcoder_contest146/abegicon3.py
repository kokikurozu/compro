import itertools

N = int(input())
xy=[list(map(int,input().split()))for _ in range(N)]
list_N = [i for i in range(N)]

kyori = 0
p_list = list(itertools.permutations(list_N))
for j in p_list:
    for i in range(len(j)):
        kyori += ((xy[j[i-1]][0] - xy[j[i]][0])**2 + (xy[j[i-1]][1] - xy[j[i]][1])**2) ** 0.5
print(kyori/len(p_list))
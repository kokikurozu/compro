import itertools
l=[-3, 2, 1, -2, 0, 5, -1 , -1]
for c  in itertools.combinations(l, 3):
    if sum(c) == 0:
        print(c)

a=open(0).read().split()
print('YNeos'[all(t-set(map(a.index,a[9:]))
for t in({0,3,6},{0,4,8},{2,4,6},{2,5,8},{3,4,5},{6,7,8}))::2])
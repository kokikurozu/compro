N = 15
listA = [2*i +1 for i in range(N)]
#print(listA)

def get_integral_value_combination(list, target):
    def a(idx, l, r, t):
        if t == sum(l): r.append(l)
        elif t < sum(l): return
        for u in range(idx, len(list)):
            a((u + 1), l + [list[u]], r, t)
        return r
    return a(0, [], [], target)

print(get_integral_value_combination(listA, (N**2) / 3))
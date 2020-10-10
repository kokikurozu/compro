listA = [5, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_integral_value_combination(list, target):
    def a(idx, l, r, t):
        if t == sum(l): r.append(l)
        elif t < sum(l): return
        for u in range(idx, len(list)):
            a((u + 1), l + [list[u]], r, t)
        return r
        return a(0, [], [], target)

print(get_integral_value_combination(listA, 10))


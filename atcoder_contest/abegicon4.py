import bisect

seq = [1, 5, 4, 3, 8, 6, 9, 7, 2, 4]

LIS = [seq[0]]
for i in range(len(seq)):
    if abs(seq[i] - LIS[-1]) > 3:
        LIS.append(seq[i])
    else:
        LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]

print(len(LIS))
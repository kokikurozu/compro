seq = [1, 5, 4, 3, 8, 6, 9, 7, 2, 4]

def LIS(L):
  from bisect import bisect
  seq=[]
  for i in L:
    pos=bisect(seq,i)
    if len(best)<=pos:
      seq.append(i)
    else:
      seq[pos]=i
  return len(seq)

print(LIS(seq))
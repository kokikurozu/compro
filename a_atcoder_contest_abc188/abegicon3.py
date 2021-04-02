n = int(input())
ai = list(map(int,input().split()))
left_ai = ai[:(2**n//2)]
right_ai = ai[(2**n//2):]
left_max = max(left_ai)
right_max = max(right_ai)

print(ai.index(min(left_max,right_max))+1)
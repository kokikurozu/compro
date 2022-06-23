s = list(input())
t = list(input())

def judge(x,y):
    if x == y:
        return 'Yes'
    for i in range(len(s)-1):
        if x[i] != y[i]:
            if x[i] == y[i+1] and x[i+1] == y[i]:
                return 'Yes'
            else:
                return 'No'
    return 'No'

print(judge(s,t))
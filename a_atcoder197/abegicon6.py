import numpy as np

def prog(x1, y1, x2, y2, x3, y3, x4, y4):
    if x1 == x2 and x3 == x4:
        x = y = np.nan
    elif x1 == x2:
        x = x1
        y = (y4 - y3) / (x4 - x3) * (x1 - x3) + y3
    elif x3 == x4:
        x = x3
        y = (y2 - y1) / (x2 - x1) * (x3 - x1) + y1
    else:
        a1 = (y2-y1)/(x2-x1)
        a3 = (y4-y3)/(x4-x3)
        if a1 == a3:
            x = y = np.nan
        else:
            x = (a1*x1-y1-a3*x3+y3)/(a1-a3)
            y = (y2-y1)/(x2-x1)*(x-x1)+y1
    return (x, y)

n = int(input())
x,y = map(int,input().split())
x1,y1 = map(int,input().split())
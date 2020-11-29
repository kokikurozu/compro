if C[p1-1][p2] == '.' and (reach[p1-1][p2] > reach[p1][p2] + 1):
        reach[p1-1][p2] = reach[p1][p2] + 1
        q1.append(p1-1)
        q2.append(p2)

    if C[p1+1][p2] == '.' and (reach[p1+1][p2] > reach[p1][p2] + 1):
        reach[p1+1][p2] = reach[p1][p2] + 1
        q1.append(p1+1)
        q2.append(p2)

    if C[p1][p2-1] == '.' and (reach[p1][p2-1] > reach[p1][p2] + 1):
        reach[p1][p2-1] = reach[p1][p2] + 1
        q1.append(p1)
        q2.append(p2-1)
    
    if C[p1][p2+1] == '.' and (reach[p1][p2+1] > reach[p1][p2] + 1):
        reach[p1][p2+1] = reach[p1][p2] + 1
        q1.append(p1)
        q2.append(p2+1)
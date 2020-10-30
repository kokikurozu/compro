N = int(input())
S = str(input())
new_S = ''
for i in S: 
    if ord(i) + N <= 90:
        new_S += chr(ord(i) + N)
    else:
        new_S += chr(ord(i) + N - 26)
print(new_S)
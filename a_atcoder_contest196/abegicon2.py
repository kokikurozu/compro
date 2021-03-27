x = input()
if '.' in x:
    x = x[:x.index('.')]
print(int(x))
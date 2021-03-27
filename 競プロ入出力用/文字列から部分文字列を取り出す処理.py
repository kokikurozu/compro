def main():
    n = input()
    x = n[:(len(n)//2)]
    y = n[(len(n)//2):]
    print(x)
    print(y)
    x = input()
    if '.' in x:
        x = x[:x.index('.')]
    print(int(x))
main()
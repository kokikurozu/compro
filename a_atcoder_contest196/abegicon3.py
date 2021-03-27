def main():
    n = input()
    if len(n) % 2 == 1:
        print(10 ** (len(n)//2) - 1)
        ""
    else:
        x = n[:((len(n)+1)//2)]
        y = n[((len(n)+1)//2):]
        x = int(x)
        try:
            y = int(y)
        except:
            y = 0
        if x <= y:
            print(x)
        else:
            print(x-1)        

if __name__ == "_main_":
    main()

main()
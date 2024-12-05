def incdec(n, num):
    if (n<1 or n>num):
        return
    else:
        print(n)
        incdec(n-1,num)
        print(n)
n = int(input("Enter: "))
incdec(n,n)
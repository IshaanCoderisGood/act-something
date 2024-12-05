def head(n,num):
    if n>num:
        return
    else:
        head(n + 1, num)
        print(n)
n = int(input("Enter: "))
head(1, n)
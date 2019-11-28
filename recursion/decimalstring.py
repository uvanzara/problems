def dshelper(slate, n):
    if n == 0:
        print(slate)
    else:
        for i in range(10):
            dshelper(slate + str(i), n - 1)

def decimalString(n):
    dshelper("", n)

if __name__ == "__main__":
    decimalString(2)


def binaryString(s):
    result = []
    def bshelper(slate, array):
        if len(array) == 0:
            result.append(slate)
        else:
            bshelper(slate, array[1:])
            bshelper(slate+array[0],  array[1:])

    bshelper("", s)
    print(result)

if __name__ == "__main__":
    binaryString("xy")

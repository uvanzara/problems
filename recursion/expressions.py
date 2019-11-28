def generate_all_expressions(s, target):
    output = set()

    
    def subexpression(s, i, slate, op):
        if i == len(s):
            # print(process(slate))
            output.add(tuple(process(slate)))
            return
        
        
        for op in ["", "+", "*"]:
            if i < len(s) - 1:
                slate.append(s[i]+op)
            else:
                slate.append(s[i])
            #print("after appending, string = {}".format(string))
            subexpression(s, i+1, slate, op)
            slate.pop()
            #if i < len(s) - 1:
            #    slate.pop()


    subexpression(s, 0, [], "")
    print("output = {}".format(list(output)))
    return output

def process(string):
    result = []
    # print('got string as {}'.format(string))
    for i in range(len(string)-1):
        if '+' in string[i]:
            result.append(string[i].split("+")[0])
        elif '*' in string[i]:
            result.append(string[i].split("+")[0])
        else:
            result.append(string[i]+string[i+1])

    return result

if __name__ == "__main__":
    generate_all_expressions('123', 11)
def generate_palindromic_decompositions(s):
    if not s or len(s) == 1:
        return [s]

    output = []
    n = len(s)

    def helper(so_far, start):
        if start == n:
            output.append('|'.join(so_far))
        
        # for start in range(len(s)-1):
            #print("start = {}".format(start))
        for i in range(start+1, n+1):
            slate = s[start:i]
            if isPalindrome(slate):
                so_far.append(slate)
            #print("size = {}".format(size))
            # print("appending {}".format(s[start:size]))
            # slate.append(s[start:size])
            #print("post appending, slate = {}".format(slate))
            #print("calling helper with {}".format(slate))
                helper(so_far, i)
                so_far.pop()
        
    helper([], 0)
    return output

def isPalindrome(s):
    if not s or len(s) == 1:
        return True
    if s == s[::-1]:
        return True
    return False

if __name__ == "__main__":
    print(generate_palindromic_decompositions("abccba"))
    print(generate_palindromic_decompositions("abracadabra"))
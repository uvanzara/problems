"""
LeetCode Problem # 784
https://leetcode.com/problems/letter-case-permutation/
"""

def letterCasePermutation(S):
    result = []
    
    def gen_letter_helper(string, i, slate):
        # base case
        if i == len(string):
            result.append(slate)
            return
        else:
            if string[i].isdigit():
                gen_letter_helper(string, i + 1, slate + string[i])
            elif string[i].isalpha():
                gen_letter_helper(string, i + 1, slate + string[i].lower())
                gen_letter_helper(string, i + 1, slate + string[i].upper())

    gen_letter_helper(S, 0, '')
    print(result)

if __name__ == "__main__":
    letterCasePermutation("a1b2")

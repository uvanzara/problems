"""
LeetCode Problem # 78
https://leetcode.com/problems/subsets/
"""

def subsets(nums):
    #result = []

    def subset_helper(nums, i, slate, result):
        if i == len(nums):
            result.append(slate[:])
        else:
            # Exclusion case
            subset_helper(nums, i + 1, slate, result)

            # Inclusion case
            slate.append(nums[i])
            subset_helper(nums, i + 1, slate, result)
            slate.pop()
        return result
    return subset_helper(nums, 0, [], [])
    # return result


if __name__ == "__main__":
    print(subsets([1,2,3,4]))
    print(subsets("abba"))


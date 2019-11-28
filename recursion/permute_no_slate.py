"""
LeetCode Problem # 46, Permutations
https://leetcode.com/problems/permutations/

This is without using slate
"""

def permute(nums):
    result = []

    def helper(nums, i):
        if len(nums) == i:
            result.append(nums[:i])
        else:
            for pick in range(i, len(nums)):
                '''
                without the swap, we will get a single element repeated over
                and over as the solution!
                '''
                nums[i], nums[pick] = nums[pick], nums[i]
                #slate.append(nums[i])
                helper(nums, i + 1)
                #slate.pop()
                nums[i], nums[pick] = nums[pick], nums[i]

    helper(nums, 0)
    return result


if __name__ == "__main__":
    nums = [1,2,3,4]
    print(permute(nums))
"""
LeetCode Problem # 90
https://leetcode.com/problems/subsets-ii/
"""

def subsets(nums):
    result = []

    def subset_helper(nums, i, slate):
        if i == len(nums):
            result.append(slate[:])
        else:
            count = 1
            current = nums[i]
            temp_i = i
            while (temp_i + 1) < len(nums) and nums[temp_i+1] == current:
                count +=1
                temp_i += 1
            #print("num = {}, count = {}".format(nums[i], count))
            # Exclusion case
            subset_helper(nums, i + count, slate)

            # Inclusion case
            for j in range(count):
                # print("appending num {} to slate".format(nums[i]))
                slate.append(nums[i])
                # print("got slate as {}".format(slate))
                subset_helper(nums, i + count, slate)
            for j in range(count):
                # print("popping {}".format(nums[i]))
                slate.pop()
    nums.sort()
    subset_helper(nums, 0, [])
    return result


if __name__ == "__main__":
    answer = subsets([1,1,1,1,2,3,4,5])
    print(sorted(answer))
    print(subsets([1,2,2]))


'''
LeetCode Problem # 113
https://leetcode.com/problems/path-sum-ii/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []
        if root is None:
            return result

        def helper(node, partial_path, targetsum, curr_sum):
            if node.left is None and node.right is None:
                if curr_sum == sum:
                    partial_path.append(node.val)
                    result.append(partial_path[:])
                    partial_path.pop()

            if node.left is not None:
                partial_path.append(node.val)
                helper(node.left, partial_path, targetsum, curr_sum + node.left.val)
                partial_path.pop()

            if node.right is not None:
                partial_path.append(node.val)
                helper(node.right, partial_path, targetsum, curr_sum + node.right.val)
                partial_path.pop()

        helper(root, [], sum, root.val)
        return result
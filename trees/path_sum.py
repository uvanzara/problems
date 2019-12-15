'''
LeetCode Problem # 112
https://leetcode.com/problems/path-sum/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if root is None:
        return False

    path = [False]
    
    def helper(node, targetsum, curr_sum):
        if node.left is None and node.right is None:
            if curr_sum == sum:
                path[0] = True
            
        if node.left is not None:
            helper(node.left, targetsum, curr_sum + node.left.val)
            
        if node.right is not None:
            helper(node.right, targetsum, curr_sum + node.right.val)
            
    helper(root, sum, root.val)
    return path[0]
'''
LeetCode # 250 Count Univalue subtrees
https://leetcode.com/problems/count-univalue-subtrees/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        univalcount = [0]
        if root is None:
            return univalcount[0]

        def dfs(node):
            # base case
            if node.left is None and node.right is None:
                univalcount[0] += 1
                return True

            # recursive case
            amiunival = True
            left = True
            right = True

            if node.left is not None:
                left = dfs(node.left)
                if not left or node.val != node.left.val:
                    amiunival = False

            if node.right is not None:
                right = dfs(node.right)
                if not right or node.val != node.right.val:
                    amiunival = False

            if amiunival:
                univalcount[0] += 1
            return amiunival

        dfs(root)
        return univalcount[0]

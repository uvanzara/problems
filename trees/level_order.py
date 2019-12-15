'''
LeetCode # 102: Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
'''

import queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):  # -> List[List[int]]:
        if root is None:
            return []
        result = []

        q = queue.Queue()
        q.put(root)

        while not q.empty():
            numnodes = q.qsize()
            temp = []
            # node = q.get()
            # temp.append(node.val)
            for i in range(numnodes):
                node = q.get()
                temp.append(node.val)
                # temp.append(node.val)
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
            result.append(temp)

        return result

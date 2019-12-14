def isBST(root):
        
    def isBSTHelper(root, prev):
        if root is None:
            return True
        
        isLeftSubtreeBST = isBSTHelper(root.left_ptr, prev)
        print('isLeftSubtreeBST = {}, prev = {}'.format(isLeftSubtreeBST, prev))
        
        if root.val < prev:
            return False
        
        prev = root.val
        print('setting prev to {}'.format(prev))
        
        isRightSubtreeBST = isBSTHelper(root.right_ptr, prev)
        print('isRightSubtreeBST = {}, prev = {}'.format(isRightSubtreeBST, prev))
        
        return isLeftSubtreeBST and isRightSubtreeBST
        
    if root is None:
        return True
    
    return isBSTHelper(root, 0)


5
300 200 400 100 400
0
4
0 1 L
0 2 R
1 3 L
1 4 R
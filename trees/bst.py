import random


class TreeNode(object):
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, root, key):
        newnode = TreeNode(key)
        if root is None:
            return newnode
        curr = root
        prev = None
        while curr:
            if curr.key == key:
                print("Key already exists!")
                return root
            elif curr.key < key:
                prev = curr
                curr = curr.right
            else:
                prev = curr
                curr = curr.left
        if key < prev.key:
            prev.left = newnode
        else:
            prev.right = newnode
        return root

    def display(self, node):
        # curr = root
        if node is None:
            return
        print("key = {}".format(node.key))
        self.display(node.left)
        self.display(node.right)


if __name__ == "__main__":
    # print("in main!")
    tn = TreeNode(random.randint(0, 100))
    for i in range(10):
        key = random.randint(0, 100)
        print("inserting key {}".format(key))
        tn.insert(tn, key)
    # pdb.set_trace()
    tn.display(tn)

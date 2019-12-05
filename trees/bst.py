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

    def search(self, root, key):
        curr = root
        while curr is not None:
            if key == curr.key:
                return curr
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        return None  # Key not found!

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
    input = []
    for i in range(10):
        input.append(random.randint(0, 100))
    print("input keys = {}".format(input))
    for key in input:
        # print("inserting key {}".format(key))
        tn.insert(tn, key)
    # pdb.set_trace()
    tn.display(tn)

    searchfor = random.choice(input)
    found = tn.search(tn, searchfor)
    if found:
        print("found {} in the tree".format(searchfor))
    else:
        print("{} not found in the tree!".format(searchfor))

    searchfor = random.randint(101, 200)
    found = tn.search(tn, searchfor)
    if found:
        print("found {} in the tree".format(searchfor))
    else:
        print("{} not found in the tree!".format(searchfor))
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

    def display_pre_order(self, node):
        if node is None:
            return
        print("key = {}".format(node.key))
        self.display_pre_order(node.left)
        self.display_pre_order(node.right)

    def display_in_order(self, node):
        if node is None:
            return
        self.display_in_order(node.left)
        print("key = {}".format(node.key))
        self.display_in_order(node.right)

    def display_post_order(self, node):
        if node is None:
            return
        self.display_post_order(node.left)
        self.display_post_order(node.right)
        print("key = {}".format(node.key))

    def findmin(self, root):
        if root is None:
            return None
        curr = root
        while curr.left is not None:
            curr = curr.left
        return curr.key

    def findmax(self, root):
        if root is None:
            return None
        curr = root
        while curr.right is not None:
            curr = curr.right
        return curr.key


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
    print("Pre-order traversal")
    tn.display_pre_order(tn)
    print("In-order traversal")
    tn.display_in_order(tn)
    print("Post-order traversal")
    tn.display_post_order(tn)

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

    print("min element in tree is {}".format(tn.findmin(tn)))
    print("max element in tree is {}".format(tn.findmax(tn)))


# This program does all simple CRUD on binary search tree
class bst:
    def __init__(self, root):
        self.left = None
        self.right = None
        self.root = root

    def search(self, node):
		if node < self.root:
			if self.left:
				return self.left.search(node)
			else:
				return "Not Found"
		elif node > self.root:
			if self.right:
				return self.right.search(node)
			else:
				return "Not Found"
		else:
			return "Found"
			

    def insert(self, node):
        if node == self.root:
            return "Node is already inserted"
        if node < self.root:
            if self.left is None:
                self.left = bst(node)
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = bst(node)
            else:
                self.right.insert(node)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print self.root,
        if self.right:
            self.right.print_tree()


if __name__ == "__main__":
    print "Binary search tree"
    root = 5
    t = bst(root)
    t.insert(8)
    t.insert(3)
    t.insert(1)
    t.insert(10)
    print t.insert(5)
    print t.search(11)
    t.print_tree()

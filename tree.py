class Tree:
	def __init__(self, root):
		self.root = root
		self.left = None
		self.right = None
	
	def insert(self, node):
		if self.root == None:
			self.root = node
		else:
			if node < self.root:
				if self.left == None:
					self.left = Tree(node)
				else:
					self.left.insert(node)
			else:
				if self.right ==  None:
					self.right = Tree(node)
				else:
					self.right.insert(node)

	def print_root(self):
		print "root is", self.root
	
	def print_tree(self):
		if self.left:
			self.left.print_tree()
		print self.root,
		if self.right:
			self.right.print_tree()

	def search(self, node):
		if node > self.root:
			if self.right:
				return self.right.search(node)
			else:
				return str(node)+" Node Not Found"
		elif node < self.root:
			if self.left:
				return self.left.search(node)
			else:
				return str(node)+" Not found"
		else:
			return str(node)+" Node found"

def mindepth(root):
		if root is None:
			return 0
		if root.left is None and root.right is None:
			return 1
		if root.left is None:
			return mindepth(root.right)+1
		if root.right is None:
			return mindepth(root.left)+1
		return min(mindepth(root.left), mindepth(root.right))+1
			


if __name__ == "__main__":
	print "in main"
	root = 2
	t = Tree(root)
	t.print_root()
	t.insert(8)
	t.insert(1)
	t.insert(0)
	t.insert(10)
	t.print_tree()
	print "\n"
	print t.search(2)
	print t.search(1)
	print t.search(8)
	print t.search(18)
	tree = Tree(4)
	tree.left = Tree(5)
	tree.right = Tree(6)
	tree.left.left = Tree(9)
	print mindepth(tree)

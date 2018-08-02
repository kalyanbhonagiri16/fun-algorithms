# Linked list CRUD with reverse linked list
class Node:
	def __init__(self):
		self.node = None
		self.next = None

class linked:
	def __init__(self):
		self.head = None
		#self.node = node
		#self.next = None

	def add(self, node):
		s = Node()
		s.node = node
		s.next = self.head
		self.head = s

	def print_list(self):
		curr = self.head
		while curr.next:
			print curr.node
			curr = curr.next
		print curr.node

	def reverse(self):
		prev = None
		curr = self.head
		while curr is not None:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		self.head = prev
			
		
if __name__ == "__main__":
	print "hello"
	l = linked()
	l.add(5)
	l.add(15)
	l.add(3)
	l.add(18)
	l.add(24)
	l.print_list()
	l.reverse()
	print "\n"
	l.print_list()

# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the
# stairs.
class steps:
	def __init__(self, n):
		self.n = n

	def total_ways(self):
		if self.n == 1:
			return 1
		elif self.n == 2:
			return 3
		else:
			return self.factorial(self.n) 

	def factorial(self, n):
		val = 1
		for i in range(2, n+1):
			val = val*i
		return val

if __name__ == "__main__":
	n = 5
	s = steps(n)
	print s.total_ways()


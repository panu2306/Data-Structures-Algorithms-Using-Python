class ArrayStack:
	def __init__(self):
		self.data = []
	
	def __len__(self):
		return len(self.data)

	def is_empty(self):
		"""Returns True if stack is empty"""
		return len(self.data) == 0

	def push(self, e):
		"""Pushes an element into a stack"""
		self.data.append(e)

	def top(self):
		"""Returns the recently added element into stack"""
		if(self.is_empty):
			raise Empty("Stack is empty")
		return self.data[-1]

	def pop(self):
		"""Pops out the top of stack"""
		if(self.is_empty):
			raise Empty("Stack is empty")
		self.data.pop()


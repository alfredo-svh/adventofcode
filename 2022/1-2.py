
# Advent of Code 22

# Day 1, Part 2


class Stack:
	def __init__(self):
		self.container = [0, 0, 0]
	
	def insert(self, num):
		if num < self.container[-1]:
			return

		if num > self.container[0]:
			self.container.insert(0, num)
		elif num > self.container[1]:
			self.container.insert(1, num)
		else:
			self.container.insert(2, num)
		
		self.container.pop()
	
	def total(self):
		return sum(self.container)


top3 = Stack()

with open("1_input.txt", "r") as f:
	lines = f.readlines()


top_cal = []

cur_cal = 0

for l in lines:
	l = l.strip()

	if l:
		cur_cal += int(l)
	else:
		top3.insert(cur_cal)
		cur_cal = 0

print(top3.total())

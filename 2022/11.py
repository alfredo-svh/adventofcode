
# Advent of Code 22

# Day 11


PART2 = True


class Monkey:
	def __init__(self, id, items) -> None:
		self.id = id
		self.items = items
		self.inspection_count = 0

	def operate(self, item_id):
		self.inspection_count += 1
		old = self.items[item_id]

		if self.id == 0:
			self.items[item_id] = old * 7
		elif self.id == 1:
			self.items[item_id] = old + 3
		elif self.id == 2:
			self.items[item_id] = old + 4
		elif self.id == 3:
			self.items[item_id] = old + 5
		elif self.id == 4:
			self.items[item_id] = old * 5
		elif self.id == 5:
			self.items[item_id] = old * old
		elif self.id == 6:
			self.items[item_id] = old + 8
		elif self.id == 7:
			self.items[item_id] = old + 1
		
		if not PART2:
			self.items[item_id] = self.items[item_id] // 3
	
	def test(self, item_id):
		item = self.items[item_id]

		if self.id == 0:
			if item % 2 == 0:
				return 7
			else:
				return 1
		elif self.id == 1:
			if item % 7 == 0:
				return 2
			else:
				return 4
		elif self.id == 2:
			if item % 13 == 0:
				return 5
			else:
				return 4
		elif self.id == 3:
			if item % 19 == 0:
				return 6
			else:
				return 0
		elif self.id == 4:
			if item % 11 == 0:
				return 5
			else:
				return 3
		elif self.id == 5:
			if item % 5 == 0:
				return 6
			else:
				return 3
		elif self.id == 6:
			if item % 3 == 0:
				return 0
			else:
				return 7
		elif self.id == 7:
			if item % 17 == 0:
				return 2
			else:
				return 1
		

def take_turn(monkey: Monkey):
	for i in range(len(monkey.items)):
		monkey.operate(i)
		to = monkey.test(i)
		monkeys[to].items.append(monkey.items[i])
	monkey.items = []
			


monkeys = [
	Monkey(0, [62, 92, 50, 63, 62, 93, 73, 50]),
	Monkey(1, [51, 97, 74, 84, 99]),
	Monkey(2, [98, 86, 62, 76, 51, 81, 95]),
	Monkey(3, [53, 95, 50, 85, 83, 72]),
	Monkey(4, [59, 60, 63, 71]),
	Monkey(5, [92, 65]),
	Monkey(6, [78]),
	Monkey(7, [84, 93, 54]),
]

if PART2:
	rounds = 1000
else:
	rounds = 20

for i in range(rounds):
	for monkey in monkeys:
		take_turn(monkey)
	print(i)


top2 = sorted([monkey.inspection_count for monkey in monkeys])[-2:]
print(top2[0] * top2[1])
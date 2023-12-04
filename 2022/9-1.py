
# Advent of Code 22

# Day 9, Part 1

class Point:
	def __init__(self, x=0, y=0) -> None:
		self.x = x
		self.y = y

	def __eq__(self, __o: object) -> bool:
		if self.x == __o.x and self.y == __o.y:
			return True
		
		return False

	def copy(self):
		return Point(self.x, self.y)


def move_tail():
	diff_x = abs(head.x - tail.x)
	diff_y = abs(head.y - tail.y)

	# No movement
	if diff_x < 2 and diff_y < 2:
		return
	
	# Vertical movement
	if diff_x == 0:
		if head.y < tail.y:
			tail.y -= 1
		else:
			tail.y += 1
	
	# Horizontal movement
	elif diff_y == 0:
		if head.x < tail.x:
			tail.x -= 1
		else:
			tail.x += 1

	# Diagonal movement
	else:
		if head.x > tail.x:
			tail.x += 1
		else:
			tail.x -= 1
		
		if head.y > tail.y:
			tail.y += 1
		else:
			tail.y -= 1

	# Update points visited
	cur_point = tail.copy()
	if cur_point not in points_visited:
		points_visited.append(cur_point)

	

def move_head_tail(dir):
	if dir == "U":
		head.y -= 1
	elif dir == "D":
		head.y += 1
	elif dir == "L":
		head.x -= 1
	elif dir == "R":
		head.x += 1

	move_tail()


with open("9_input.txt", "r") as f:
	lines = f.readlines()


head = Point()
tail = Point()
points_visited = [Point()]


for line in lines:
	line = line.strip()

	dir, moves = line.split()

	for move in range(int(moves)):
		move_head_tail(dir)

print(len(points_visited))
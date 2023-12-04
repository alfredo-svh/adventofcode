
# Advent of Code 22

# Day 9, Part 2

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


def move_knot(index):
	knot = knots[index]
	prev = knots[index-1]

	diff_x = abs(prev.x - knot.x)
	diff_y = abs(prev.y - knot.y)

	# No movement
	if diff_x < 2 and diff_y < 2:
		return
	
	# Vertical movement
	if diff_x == 0:
		if prev.y < knot.y:
			knot.y -= 1
		else:
			knot.y += 1
	
	# Horizontal movement
	elif diff_y == 0:
		if prev.x < knot.x:
			knot.x -= 1
		else:
			knot.x += 1

	# Diagonal movement
	else:
		if prev.x > knot.x:
			knot.x += 1
		else:
			knot.x -= 1
		
		if prev.y > knot.y:
			knot.y += 1
		else:
			knot.y -= 1

	# Update points visited
	if knot is tail:
		cur_point = knot.copy()
		if cur_point not in points_visited:
			points_visited.append(cur_point)

	

def move_head(dir):
	if dir == "U":
		head.y -= 1
	elif dir == "D":
		head.y += 1
	elif dir == "L":
		head.x -= 1
	elif dir == "R":
		head.x += 1

	for i in range(1, len(knots)):
		move_knot(i)


with open("9_input.txt", "r") as f:
	lines = f.readlines()


knots = [Point() for _ in range(10)]
head = knots[0]
tail = knots[-1]
points_visited = [Point()]


for line in lines:
	line = line.strip()

	dir, moves = line.split()

	for move in range(int(moves)):
		move_head(dir)

print(len(points_visited))
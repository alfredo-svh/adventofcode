
# Advent of Code 22

# Day 8


def is_hidden(lat, lon):
	size = grid[lat][lon]

	# from top
	if lat == 0:
		return 0

	for i in range(lat):
		if grid[i][lon] >= size:
			break
	else:
		return 0

	# from bottom
	if lat == len(grid) - 1:
		return 0

	for i in range(len(grid)-1, lat, -1):
		if grid[i][lon] >= size:
			break
	else:
		return 0

	# from left
	if lon == 0:
		return 0
	
	for j in range(lon):
		if grid[lat][j] >= size:
			break
	else:
		return 0

	# from right
	if lon == len(grid[0]) - 1:
		return 0

	for j in range(len(grid[0])-1, lon, -1):
		if grid[lat][j] >= size:
			break
	else:
		return 0

	return 1

def scenic_score(lat, lon):
	size = grid[lat][lon]

	# up
	up = 0
	if lat == 0:
		return 0

	for i in range(lat-1, -1, -1):
		up += 1
		if grid[i][lon] >= size:
			break

	# down
	down = 0
	if lat == len(grid) - 1:
		return 0

	for i in range(lat+1, len(grid)):
		down += 1
		if grid[i][lon] >= size:
			break

	# left
	left = 0
	if lon == 0:
		return 0
	
	for j in range(lon-1, -1, -1):
		left += 1
		if grid[lat][j] >= size:
			break

	# right
	right = 0
	if lon == len(grid[0]) - 1:
		return 0

	for j in range(lon+1, len(grid[0])):
		right += 1
		if grid[lat][j] >= size:
			break
	
	return up * down * left * right


with open("8_input.txt", "r") as f:
	lines = f.readlines()

# Create 2D array
grid = []
for line in lines:
	line = line.strip()
	grid.append([int(x) for x in line])


# Part 1: Count hidden trees
hidden = 0
for i in range(len(grid)):
	for j in range(len(grid[0])):
		hidden += is_hidden(i, j)

print(len(grid) * len(grid[0]) - hidden)

# Part 2: Find highest scenic score
highest = 0
for i in range(len(grid)):
	for j in range(len(grid[0])):
		cur_score = scenic_score(i, j)
		highest = max(cur_score, highest)

print(highest)
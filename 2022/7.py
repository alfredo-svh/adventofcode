
# Advent of Code 22

# Day 7


class File:
	def __init__(self, name, size) -> None:
		self.name = name
		self.size = size
	
	def __str__(self) -> str:
		return self.name


class Directory:
	def __init__(self, name, parent=None) -> None:
		self.name = name
		self.parent = parent
		self.children = {}
		self.size = 0

	def __str__(self) -> str:
		out = self.name
		for c in self.children.values():
			out += f"\n {c.name}"
		
		return out

	def return_sum_small(self):
		total = 0

		for c in self.children.values():
			if type(c) == Directory:
				total += c.return_sum_small()
		
		if self.size < 100000:
			total += self.size
		
		return total

	def to_delete(self, target):
		size_to_delete = None

		for c in self.children.values():
			if type(c) == Directory:
				cur_size = c.to_delete(target)

				if cur_size and (not size_to_delete or cur_size < size_to_delete):
					size_to_delete = cur_size

		if self.size >= target and (not size_to_delete or self.size < size_to_delete):
			return self.size
		
		return size_to_delete


fs = Directory("/")
cur_directory = fs


with open("7_input.txt", "r") as f:
	lines = f.readlines()

cur_line = 1

# Fill up file system
while cur_line < len(lines) - 1:
	lines[cur_line].strip()
	args = lines[cur_line].split()

	if args[0] != "$":
		print("Error: Unexpected line")
		break

	if args[1] == "cd":
		if args[2] == "..":
			cur_directory = cur_directory.parent
		else:
			cur_directory = cur_directory.children[args[2]]

		cur_line += 1

	elif args[1] == "ls":
		cur_line += 1
		lines[cur_line].strip()
		args = lines[cur_line].split()

		while args[0] != "$":
			if args[0] == "dir":
				cur_directory.children[args[1]] = Directory(args[1], cur_directory)
			else:
				cur_directory.children[args[1]] = File(args[1], int(args[0]))

				tmp_dir = cur_directory
				while tmp_dir:
					tmp_dir.size += int(args[0])
					tmp_dir = tmp_dir.parent

			cur_line += 1
			if cur_line < len(lines):
				lines[cur_line].strip()
				args = lines[cur_line].split()
			else:
				break


# Part 1
print("# Part 1")
print(fs.return_sum_small())

# Part 2
print("\n# Part 2")
space_needed = 30000000 - (70000000 - fs.size)
print(fs.to_delete(space_needed))
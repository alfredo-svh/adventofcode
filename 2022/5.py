
# Advent of Code 22

# Day 5


PART_2 = True


def move_stacks(arr):
	quantity = int(arr[0])
	s_from = int(arr[1])
	s_to = int(arr[2])

	move = stacks[s_from-1][-quantity:]
	stacks[s_from-1] = stacks[s_from-1][:-quantity]

	if not PART_2:
		move.reverse()
	stacks[s_to-1].extend(move)


# manually build the stacks from input file
stacks = [
	["J", "H", "G", "M", "Z", "N", "T", "F"],
	["V", "W", "J"],
	["G", "V", "L", "J", "B", "T", "H"],
	["B", "P", "J", "N", "C", "D", "V", "L"],
	["F", "W", "S", "M", "P", "R", "G"],
	["G", "H", "C", "F", "B", "N", "V", "M"],
	["D", "H", "G", "M", "R"],
	["H", "N", "M", "V", "Z", "D"],
	["G", "N", "F", "H"]
]



with open("5_input.txt", "r") as f:
	lines = f.readlines()

# Remove the lines with information about the starting status of the stack
lines = lines[10:]

for l in lines:
	l = l.strip()

	l = l.replace("move ", "")
	l = l.replace("from ", "")
	l = l.replace("to ", "")

	move_stacks(l.split(" "))


for stack in stacks:
	print(stack[-1], end="")

# Advent of Code 22

# Day 3, Part 2


def get_repeated(group: list):
	for i in group[0].strip():
		for j in group[1].strip():
			for k in group[2].strip():
				if i == j and j == k:
					return i

def get_priority(letter: str):
	ascii = ord(letter)
	if letter.islower():
		return ascii - ord('a') + 1

	return ascii - ord('A') + 27



with open("3_input.txt", "r") as f:
	lines = f.readlines()

priorities_sum = 0

groups = [[lines[i], lines[i+1], lines[i+2]] for i in range(0, len(lines), 3)]

for group in groups:
	badge = get_repeated(group)
	priorities_sum += get_priority(badge)


print(priorities_sum)
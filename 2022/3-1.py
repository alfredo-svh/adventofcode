
# Advent of Code 22

# Day 3, Part 1


def get_repeated(c1: str, c2: str):
	for i in c1:
		for j in c2:
			if i == j:
				return i

def get_priority(letter: str):
	ascii = ord(letter)
	if letter.islower():
		return ascii - ord('a') + 1

	return ascii - ord('A') + 27



with open("3_input.txt", "r") as f:
	lines = f.readlines()

priorities_sum = 0

for l in lines:
	l = l.strip()
	len_cmpt = len(l) // 2
	c1 = l[:len_cmpt]
	c2 = l[len_cmpt:]

	repeated = get_repeated(c1, c2)
	priorities_sum += get_priority(repeated)


print(priorities_sum)
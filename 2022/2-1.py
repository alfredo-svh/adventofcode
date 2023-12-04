
# Advent of Code 22

# Day 2, Part 1


def getscore(op, me):
	score = 0

	# Me: Rock
	if me == "X":
		score += 1

		# Tie
		if op == "A":
			score += 3
		# Win
		elif op == "C":
			score += 6


	# Me: Paper
	elif me == "Y":
		score += 2

		# Tie
		if op == "B":
			score += 3
		# Win
		elif op == "A":
			score += 6

	# Me: Scissors
	else:
		score += 3

		# Tie
		if op == "C":
			score += 3
		# Win
		elif op == "B":
			score += 6


	return score



with open("2_input.txt", "r") as f:
	lines = f.readlines()

score = 0

for l in lines:
	score += getscore(l[0], l[2])


print(score)

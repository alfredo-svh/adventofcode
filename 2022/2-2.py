
# Advent of Code 22

# Day 2, Part 2


def getscore(op, me):

	# Opponent: Rock
	if op == "A":

		# Tie
		if me == "Y":
			score = 3 + 1
		# Win
		elif me == "Z":
			score = 6 + 2
		# Lose
		else:
			score = 3


	# Opponent: Paper
	elif op == "B":

		# Tie
		if me == "Y":
			score = 3 + 2
		# Win
		elif me == "Z":
			score = 6 + 3
		# Lose
		else:
			score = 1

	# Opponent: Scissors
	else:

		# Tie
		if me == "Y":
			score = 3 + 3
		# Win
		elif me == "Z":
			score = 6 + 1
		# Lose
		else:
			score = 2


	return score



with open("2_input.txt", "r") as f:
	lines = f.readlines()

score = 0

for l in lines:
	score += getscore(l[0], l[2])


print(score)
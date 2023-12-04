
# Advent of Code 22

# Day 6

from collections import Counter

# MESSAGE_LEN = 4 for part 1 and 14 for part 2
MESSAGE_LEN = 14


with open("6_input.txt", "r") as f:
	lines = f.readlines()

# Remove the lines with information about the starting status of the stack
s = lines[0].strip()

for i in range(MESSAGE_LEN, len(s)):
	count = Counter(s[i-MESSAGE_LEN:i])
	if count.most_common(1)[0][1] == 1:
		print(i)
		break
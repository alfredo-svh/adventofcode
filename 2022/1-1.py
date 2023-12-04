
# Advent of Code 22

# Day 1, Part 1


with open("1_input.txt", "r") as f:
	lines = f.readlines()


max_cal = 0
cur_cal = 0

for l in lines:
	l = l.strip()

	if l:
		cur_cal += int(l)
	else:
		max_cal = max(cur_cal, max_cal)
		cur_cal = 0

print(max_cal)

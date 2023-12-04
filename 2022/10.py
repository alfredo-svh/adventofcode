
# Advent of Code 22

# Day 10


def update_signal():
	global total_signal
	global next_signal_at

	total_signal += x * next_signal_at
	next_signal_at += 40


def print_pixel():
	cur_x = (cur_cycle - 1) % 40

	if cur_x in [x-1, x, x+1]:
		print("#", end="")
	else:
		print(".", end="")

	if cur_x == 39:
		print("")


with open("10_input.txt", "r") as f:
	lines = f.readlines()

cur_cycle = 1
x = 1
next_signal_at = 20
total_signal = 0

for line in lines:
	line = line.strip()

	if line == "noop":
		print_pixel()
		if cur_cycle == next_signal_at:
			update_signal()

		cur_cycle += 1

	else:
		print_pixel()
		cur_cycle += 1
		print_pixel()

		if cur_cycle >= next_signal_at:
			update_signal()

		cur_cycle += 1
		v = int(line.split()[-1])
		x += v

print(total_signal)
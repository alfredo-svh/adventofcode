
# Advent of Code 22

# Day 4, Part 1


class Elf:
	def __init__(self, s) -> None:
		self.begins, self.ends = s.split("-")

		self.begins = int(self.begins)
		self.ends = int(self.ends)

def is_contained(elf1: Elf, elf2: Elf):
	if(elf1.begins <= elf2.begins and elf1.ends >= elf2.ends
	   or elf2.begins <= elf1.begins and elf2.ends >= elf1.ends):

		return 1
	
	return 0



with open("4_input.txt", "r") as f:
	lines = f.readlines()

fully_contained = 0

for l in lines:
	l = l.strip()
	elf1, elf2 = l.split(",")

	fully_contained += is_contained(Elf(elf1), Elf(elf2))


print(fully_contained)
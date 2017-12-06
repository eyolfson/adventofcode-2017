import argparse

def part_one(path):
	with open(path, 'r') as f:
		ns = [int(x.strip()) for x in f.readlines()]
	current_instruction = 0
	steps = 0
	while current_instruction >= 0 and current_instruction < len(ns):
		offset = ns[current_instruction]
		ns[current_instruction] += 1
		current_instruction += offset
		steps += 1
	print('Part one:', steps)

def part_two(path):
	with open(path, 'r') as f:
		ns = [int(x.strip()) for x in f.readlines()]
	current_instruction = 0
	steps = 0
	while current_instruction >= 0 and current_instruction < len(ns):
		offset = ns[current_instruction]
		if offset >= 3:
			ns[current_instruction] -= 1
		else:
			ns[current_instruction] += 1
		current_instruction += offset
		steps += 1
	print('Part two:', steps)

def main(args):
	part_one(args.path)
	part_two(args.path)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

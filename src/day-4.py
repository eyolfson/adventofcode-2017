import argparse

def is_valid(words):
	valid = True
	unique_words = set()
	for word in words:
		if word not in unique_words:
			unique_words.add(word)
		else:
			valid = False
			break
	return valid

def part_one(path):
	unique_lines = 0
	with open(path, 'r') as f:
		for line in f:
			words = line.strip().split(' ')
			if is_valid(words):
				unique_lines += 1
	print('Part one:', unique_lines)

def part_two(path):
	unique_lines = 0
	with open(path, 'r') as f:
		for line in f:
			unsorted_words = line.strip().split(' ')
			words = []
			for word in unsorted_words:
				words.append(''.join(sorted(word)))
			if is_valid(words):
				unique_lines += 1
	print('Part two:', unique_lines)

def main(args):
	part_one(args.path)
	part_two(args.path)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

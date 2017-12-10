import argparse

def swap(l, i, j):
	t = l[i]
	l[i] = l[j]
	l[j] = t

def reverse(l, current_position, length):
	start = current_position
	end = (current_position + length - 1) % len(l)
	for _ in range(length // 2):
		swap(l, start, end)
		start = (start + 1) % len(l)
		end = (end - 1) % len(l)

def knot_hash_round(l, lengths, current_position=0, skip_size=0):
	for length in lengths:
		reverse(l, current_position, length)
		current_position = (current_position + length + skip_size) % len(l)
		skip_size += 1
	return current_position, skip_size

def part_one(path):
	with open(path, 'r') as f:
		lengths = [int(x) for x in f.read().strip().split(',')]
	l = [x for x in range(256)]
	knot_hash_round(l, lengths)
	print('Part one:', l[0] * l[1])

def part_two(path):
	with open(path, 'r') as f:
		lengths = [ord(x) for x in f.read().strip()]
	lengths += [17, 31, 73, 47, 23]
	l = [x for x in range(256)]
	current_position = 0
	skip_size = 0
	for _ in range(64):
		current_position, skip_size = knot_hash_round(l, lengths, current_position, skip_size)
	h = []
	for i in range(16):
		start = i * 16
		end = (i + 1) * 16
		num = 0
		for j in range(start, end):
			num ^= l[j]
		h.append('{:02x}'.format(num))
	h = ''.join(h)
	print('Part two:', h)

def main(args):
	part_one(args.path)
	part_two(args.path)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

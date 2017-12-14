import argparse
import itertools

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

def get_row(d, c):
	lengths = [ord(x) for x in '{}-{}'.format(d, c)]
	lengths += [17, 31, 73, 47, 23]
	l = [x for x in range(256)]
	current_position = 0
	skip_size = 0
	for _ in range(64):
		current_position, skip_size = knot_hash_round(l, lengths, current_position, skip_size)
	h = []
	num_row_part = {
		'0': [0, 0, 0, 0],
		'1': [0, 0, 0, -1],
		'2': [0, 0, -1, 0],
		'3': [0, 0, -1, -1],
		'4': [0, -1, 0, 0],
		'5': [0, -1, 0, -1],
		'6': [0, -1, -1, 0],
		'7': [0, -1, -1, -1],
		'8': [-1, 0, 0, 0],
		'9': [-1, 0, 0, -1],
		'a': [-1, 0, -1, 0],
		'b': [-1, 0, -1, -1],
		'c': [-1, -1, 0, 0],
		'd': [-1, -1, 0, -1],
		'e': [-1, -1, -1, 0],
		'f': [-1, -1, -1, -1],
	}
	row = []
	for i in range(16):
		start = i * 16
		end = (i + 1) * 16
		num = 0
		for j in range(start, end):
			num ^= l[j]
		for c in '{:02x}'.format(num):
			row += num_row_part[c]
		h.append('{:02x}'.format(num))
	h = ''.join(h)
	return row

def fill(m, r, c, region):
	if r < 0 or r >= 128:
		return
	if c < 0 or c >= 128:
		return
	if m[r][c] == 0:
		return
	if m[r][c] == region:
		return
	m[r][c] = region
	fill(m, r - 1, c, region)
	fill(m, r + 1, c, region)
	fill(m, r, c- 1, region)
	fill(m, r, c + 1, region)

def main(args):
	with open(args.path, 'r') as f:
		d = f.read().strip()

	num_used = 0
	m = []
	for i in range(128):
		m.append(get_row(d, i))
		num_used += m[-1].count(-1)
	print('Part one:', num_used)

	next_region = 1
	for r in range(128):
		for c in range(128):
			if m[r][c] == -1:
				fill(m, r, c, next_region)
				next_region += 1
	print('Part two:', next_region - 1)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

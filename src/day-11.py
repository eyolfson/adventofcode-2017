import argparse

def count_steps(directions):
	coord = [0, 0, 0]
	for direction in directions:
		if direction == "n":
			coord[0] += 1
		elif direction == "nw":
			coord[1] += 1
		elif direction == "ne":
			coord[2] += 1
		elif direction == "s":
			coord[0] -= 1
		elif direction == "sw":
			coord[2] -= 1
		elif direction == "se":
			coord[1] -= 1
		else:
			assert False

	# Reductions
	# [0, 1, 1]  = [1, 0, 0] nw + ne = n
	# [1, 0, -1] = [0, 1, 0] n + sw = nw
	# [1, -1, 0] = [0, 0, 1] n + se = ne
	# [0, 1, -1]  = [-1, 0, 0] nw + s = sw
	# [-1, 0, 1] = [0, -1, 0]  s + ne = se
	# [-1, 1, 0]  = [0, 0, -1] sw + se = s

	if coord[1] > 0 and coord[2] > 0:
		m = min(coord[1], coord[2])
		coord[1] -= m
		coord[2] -= m
		coord[0] += m
	elif coord[0] > 0 and coord[2] < 0:
		m = min(abs(coord[0]), abs(coord[2]))
		coord[0] -= m
		coord[2] += m
		coord[1] += m
	elif coord[0] > 0 and coord[1] < 0:
		m = min(abs(coord[0]), abs(coord[1]))
		coord[0] -= m
		coord[1] += m
		coord[2] += m
	elif coord[1] > 0 and coord[2] < 0:
		m = min(abs(coord[0]), abs(coord[1]))
		coord[1] -= m
		coord[2] += m
		coord[0] -= m
	elif coord[0] < 0 and coord[2] > 0:
		m = min(abs(coord[0]), abs(coord[2]))
		coord[0] += m
		coord[2] -= m
		coord[1] -= m
	elif coord[0] < 0 and coord[1] > 0:
		m = min(abs(coord[0]), abs(coord[1]))
		coord[0] += m
		coord[1] -= m
		coord[2] -= m
	return abs(coord[0]) + abs(coord[1]) + abs(coord[2])

def main(args):
	with open(args.path, 'r') as f:
		directions = [x for x in f.read().strip().split(',')]

	print('Part one:', count_steps(directions))

	max_steps = count_steps(directions)
	for i in range(1, len(directions)):
		max_steps = max(max_steps, count_steps(directions[:i]))

	print('Part two:', max_steps)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

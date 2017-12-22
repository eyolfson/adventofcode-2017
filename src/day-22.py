import argparse

def main(args):
	d = [['.' for _ in range(2001)] for _ in range(2001)]
	mid = (len(d) - 1) // 2
	with open(args.path, 'r') as f:
		for j, line in enumerate(f):
			l = list(line.strip())
			cur_mid = (len(l) - 1) // 2
			for i in range(len(l)):
				y = mid + (j - cur_mid)
				x = mid + (i - cur_mid)
				d[y][x] = l[i]
	current_x = mid
	current_y = mid
	direction = 'u'

	def turn_right(h):
		return {'u': 'r', 'r': 'd', 'd': 'l', 'l': 'u'}[h]

	def turn_left(h):
		return {'u': 'l', 'l': 'd', 'd': 'r', 'r': 'u'}[h]

	num_infected = 0
	for _ in range(10000):
		if d[current_y][current_x] == '#':
			direction = turn_right(direction)
			d[current_y][current_x] = '.'
		else:
			direction = turn_left(direction)
			d[current_y][current_x] = '#'
			num_infected += 1

		if direction == 'u':
			current_y -= 1
		elif direction == 'd':
			current_y += 1
		elif direction == 'l':
			current_x -= 1
		elif direction == 'r':
			current_x += 1

		assert current_x >= 0 and current_x < len(d)
		assert current_y >= 0 and current_y < len(d)

	print('Part one:', num_infected)

	def turn_reverse(h):
		return {'u': 'd', 'd': 'u', 'l': 'r', 'r': 'l'}[h]

	d = [['.' for _ in range(2001)] for _ in range(2001)]
	mid = (len(d) - 1) // 2
	with open(args.path, 'r') as f:
		for j, line in enumerate(f):
			l = list(line.strip())
			cur_mid = (len(l) - 1) // 2
			for i in range(len(l)):
				y = mid + (j - cur_mid)
				x = mid + (i - cur_mid)
				d[y][x] = l[i]
	current_x = mid
	current_y = mid
	direction = 'u'

	num_infected = 0
	for _ in range(10000000):
		c = d[current_y][current_x]
		if c == '#':
			direction = turn_right(direction)
			d[current_y][current_x] = 'F'
		elif c == '.':
			direction = turn_left(direction)
			d[current_y][current_x] = 'W'
		elif c == 'W':
			d[current_y][current_x] = '#'
			num_infected += 1
		elif c == 'F':
			direction = turn_reverse(direction)
			d[current_y][current_x] = '.'

		if direction == 'u':
			current_y -= 1
		elif direction == 'd':
			current_y += 1
		elif direction == 'l':
			current_x -= 1
		elif direction == 'r':
			current_x += 1

		assert current_x >= 0 and current_x < len(d)
		assert current_y >= 0 and current_y < len(d)
	print('Part two:', num_infected)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

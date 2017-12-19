import argparse

def main(args):
	m = []
	with open(args.path, 'r') as f:
		for line in f:
			m.append([x for x in line[:-1]])
	h = len(m)
	w = len(m[0])
	m.append([' ' for x in range(w)])
	y = 0
	direction = 'd'
	for i in range(w):
		if m[0][i] == '|':
			x = i
	def in_range(a, b):
		if a < 0 or a >= h:
			return False
		if b < 0 or b >= w:
			return False
		return True

	def is_left_right(y, x):
		if not in_range(y, x):
			return False
		if m[y][x] == '-' or m[y][x] == '+' or m[y][x].isalpha():
			return True
		return False

	def is_up_down(y, x):
		if not in_range(y, x):
			return False
		if m[y][x] == '|' or m[y][x] == '+' or m[y][x].isalpha():
			return True
		return False

	letters = []
	steps = 1
	while True:
		if direction == 'd':
			y += 1
		elif direction == 'u':
			y -= 1
		elif direction == 'l':
			x -= 1
		elif direction == 'r':
			x += 1

		if m[y][x].isalpha():
			letters.append(m[y][x])

		if m[y][x] == ' ':
			if direction == 'd':
				y -= 1	
			elif direction == 'u':
				y += 1
			elif direction == 'l':
				x += 1
			elif direction == 'r':
				x -= 1
			steps -= 1

			if direction == 'd' or direction == 'u':
				if is_left_right(y, x + 1):
					direction = 'r'
				elif is_left_right(y, x - 1):
					direction = 'l'
				else:
					break
			else:
				if is_up_down(y - 1, x):
					direction = 'u'
				elif is_up_down(y + 1, x):
					direction = 'd'
				else:
					break
		steps += 1
	steps += 1

	print('Part one:', ''.join(letters))
	print('Part two:', steps)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

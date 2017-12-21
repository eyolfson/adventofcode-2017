import argparse

def main(args):
	rules2_3 = []
	rules3_4 = []
	with open(args.path, 'r') as f:
		for line in f:
			rule, output = [list(map(list, x.split('/'))) for x in line.strip().split(' => ')]
			if len(rule) == 2 and len(output) == 3:
				rules2_3.append((rule, output))
			elif len(rule) == 3 and len(output) == 4:
				rules3_4.append((rule, output))
			else:
				print(rule, output)
				assert False

	p = [['.', '#', '.'],
	     ['.', '.', '#'],
	     ['#', '#', '#']]

	def check(x, y, rule):
		s = len(rule)
		for swap in [False, True]:
			for invert_x in [False, True]:
				for invert_y in [False, True]:
					match = True
					for i in range(s):
						for j in range(s):
							if not invert_x:
								k = i
							else:
								k = (s - 1) - i
							if not invert_y:
								l = j
							else:
								l = (s - 1) - j
							if swap:
								k, l = l, k
							if p[x + i][y + j] != rule[k][l]:
								match = False
								break
						if not match:
							continue
					if match:
						return True
		return False

	def iteration():
		if len(p) % 2 == 0:
			s = (len(p) // 2)
			l = s * 3
			q = [['.' for _ in range(l)] for _ in range(l)]
			for x in range(0, len(p), 2):
				for y in range(0, len(p), 2):
					found = False
					for rule, output in rules2_3:
						match = check(x, y, rule)
						if match:
							found = True
							for i in range(len(output)):
								for j in range(len(output)):
									q[(x // 2 * 3) + i][(y // 2 * 3) + j] = output[i][j]
					assert found
		else:
			assert len(p) % 3 == 0
			s = (len(p) // 3)
			l = s * 4
			q = [['.' for _ in range(l)] for _ in range(l)]
			for x in range(0, len(p), 3):
				for y in range(0, len(p), 3):
					found = False
					for rule, output in rules3_4:
						match = check(x, y, rule)
						if match:
							found = True
							for i in range(len(output)):
								for j in range(len(output)):
									q[(x // 3 * 4) + i][(y // 3 * 4) + j] = output[i][j]
					assert found
		return q

	for _ in range(5):
		p = iteration()

	count = 0
	for i in range(len(p)):
		for j in range(len(p)):
			if p[i][j] == '#':
				count += 1

	print('Part one:', count)

	for _ in range(13):
		p = iteration()

	count = 0
	for i in range(len(p)):
		for j in range(len(p)):
			if p[i][j] == '#':
				count += 1

	print('Part two:', count)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

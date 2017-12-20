import argparse
import collections

def main(args):
	p = []
	v = []
	a = []

	def convert(s):
		return [int(x) for x in s[s.index('<') + 1:s.index('>')].split(',')]

	with open(args.path, 'r') as f:
		for line in f:
			ip, iv, ia = line.strip().split()
			p.append(convert(ip))
			v.append(convert(iv))
			a.append(convert(ia))

	def accel_rate(t):
		return abs(t[0]) + abs(t[1]) + abs(t[2])

	min_accel_index = 0
	min_accel = accel_rate(a[min_accel_index])
	for i in range(1, len(a)):
		cur_accel = accel_rate(a[i])
		if cur_accel < min_accel:
			min_accel = cur_accel
			min_accel_index = i
	print('Part one:', min_accel_index)

	def is_destroyed(t):
		return t[0] == 0 and t[1] == 0 and t[2] == 0

	def set_destroyed(t):
		t[0] = 0
		t[1] = 0
		t[2] = 0

	def update(i):
		for index in range(3):
			v[i][index] += a[i][index]
		for index in range(3):
			p[i][index] += v[i][index]

	for i in range(len(a)):
		assert not is_destroyed(a[i])

	num_destroyed = 0
	for _ in range(100):
		for i in range(len(a)):
			update(i)
		to_destroy = set()
		for i in range(len(a)):
			if is_destroyed(a[i]):
				continue
			for j in range(len(a)):
				if i == j:
					continue
				if is_destroyed(a[j]):
					continue
				if p[i] == p[j]:
					to_destroy.add(i)
					to_destroy.add(j)
		for i in to_destroy:
			set_destroyed(a[i])
		num_destroyed += len(to_destroy)
	print('Part two:', len(a) - num_destroyed)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

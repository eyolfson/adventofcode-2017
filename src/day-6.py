import argparse

def get_redistributions(ns):
	unique_ns = set()
	redistributions = 0
	while tuple(ns) not in unique_ns:
		unique_ns.add(tuple(ns))
		m = max(ns)
		i = 0
		while ns[i] != m:
			i += 1
		r = ns[i]
		ns[i] = 0
		for _ in range(r):
			i = (i + 1) % len(ns)
			ns[i] += 1
		redistributions += 1
	return redistributions

def main(args):
	ns = []
	with open(args.path, 'r') as f:
		for line in f:
			ns += [int(x) for x in line.strip().split()]

	print('Part one:', get_redistributions(ns))
	print('Part two:', get_redistributions(ns))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

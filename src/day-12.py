import argparse
import collections
import re

def main(args):
	d = collections.defaultdict(set)
	matcher = re.compile(r'\D+')
	with open(args.path, 'r') as f:
		for line in f:
			ns = [int(x) for x in matcher.split(line.strip())]
			for k in ns:
				for v in ns:
					d[k].add(v)
	for i in range(len(d)):
		changed = True
		while changed:
			changed = False
			vs = tuple(d[i])
			for v in vs:
				for u in d[v]:
					if u not in d[i]:
						d[i].add(u)
						changed = True
	groups = set()
	for group in d.values():
		groups.add(tuple(sorted(group)))

	print('Part one:', len(d[0]))
	print('Part two:', len(groups))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

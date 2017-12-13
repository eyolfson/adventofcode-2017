import argparse
import collections
import itertools

def severity(firewall, max_depth):
	severity = 0
	for d in range(max_depth + 1):
		if d not in firewall:
			continue
		depth_period = (firewall[d] - 1) * 2
		caught = d % depth_period == 0
		if caught:
			severity += d * firewall[d]
	return severity

def caught(firewall, max_depth, delay):
	severity = 0
	for d in range(max_depth + 1):
		if d not in firewall:
			continue
		depth_period = (firewall[d] - 1) * 2
		caught = (d + delay) % depth_period == 0
		if caught:
			return True
	return False

def main(args):
	firewall = collections.defaultdict(int)
	with open(args.path, 'r') as f:
		for line in f:
			d, r = [int(x) for x in line.strip().split(': ')]
			firewall[d] = r
	max_depth = max(firewall.keys())

	print('Part one:', severity(firewall, max_depth))
	delay = 1
	while caught(firewall, max_depth, delay):
		delay += 1
	print('Part two:', delay)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

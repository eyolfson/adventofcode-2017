import argparse
import re

printed_part_two = False

def calculate_weights(nodes, node):
	global printed_part_two
	weight, on_top = nodes[node]
	if len(on_top) == 0:
		return weight
	else:
		w = weight
		top_weights = []
		first_top_weight = None
		for n in on_top:
			top_weight = calculate_weights(nodes, n)
			top_weights.append(top_weight)
			if first_top_weight is None:
				first_top_weight = top_weight

		mismatches = 0
		for top_weight in top_weights:
			if first_top_weight != top_weight:
				mismatches += 1
		if mismatches > 0 and not printed_part_two:
			assert(mismatches == 1)
			for top_weight in top_weights:
				if first_top_weight != top_weight:
					mismatched_weight = top_weight
			d = mismatched_weight - top_weight
			for n in on_top:
				top_weight = calculate_weights(nodes, n)
				if top_weight == mismatched_weight:
					print('Part two:', nodes[n][0] - d)
			printed_part_two = True

		w = weight
		for top_weight in top_weights:
			w += top_weight
		return w

def main(args):
	matcher = re.compile(r'(\w+) \((\d+)\)( -> )?(.*)\n$')
	nodes = {}
	not_bottom = set()
	with open(args.path, 'r') as f:
		for line in f:
			m = matcher.match(line)
			node = m.group(1)
			weight = int(m.group(2))
			on_top = m.group(4).split(', ')
			if on_top == ['']:
				on_top = []
			nodes[node] = (weight, on_top)
	for n, t in nodes.items():
		w, dns = t
		for dn in dns:
			not_bottom.add(dn)
	for n in nodes.keys():
		if n not in not_bottom:
			bottom = n
	print('Part one:', bottom)
	calculate_weights(nodes, bottom)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

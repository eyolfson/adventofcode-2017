import argparse
import collections

def str1(connected_ports, i=0, value=0, visited=[]):
	strs = []
	for ports in connected_ports[i]:
		if ports in visited:
			continue
		if ports[0] == i:
			j = ports[1]
		else:
			j = ports[0]
		next_visited = visited[:]
		next_visited.append(ports)
		strs.append(str1(connected_ports, j, value + i + j, next_visited))
	if len(strs) == 0:
		return value
	return max(strs)

def str2(connected_ports, i=0, value=0, visited=[]):
	strs = []
	for ports in connected_ports[i]:
		if ports in visited:
			continue
		if ports[0] == i:
			j = ports[1]
		else:
			j = ports[0]
		next_visited = visited[:]
		next_visited.append(ports)
		strs.append(str2(connected_ports, j, value + i + j, next_visited))
	if len(strs) == 0:
		return (len(visited), value)
	return max(strs)

def main(args):
	connected_ports = collections.defaultdict(list)
	with open(args.path, 'r') as f:
		for line in f:
			p1, p2 = [int(x) for x in line.strip().split('/')]
			connected_ports[p1].append((p1, p2))
			connected_ports[p2].append((p1, p2))

	print('Part one:', str1(connected_ports))
	print('Part two:', str2(connected_ports)[1])

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

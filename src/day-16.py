import argparse
import copy

def main(args):
	moves = []
	with open(args.path, 'r') as f:
		for line in f:
			for move in line.strip().split(','):
				moves.append(move)

	s = [chr(ord('a') + x) for x in range(16)]
	sequence = []
	while ''.join(s) not in sequence:
		sequence.append(''.join(s))
		for move in moves:
			if move[0] == 's':
				size = int(move[1:])
				s = s[-size:] + s[:-size]
			elif move[0] == 'x':
				i, j = [int(x) for x in move[1:].split('/')]
				t = s[i]
				s[i] = s[j]
				s[j] = t
			elif move[0] == 'p':
				x, y = move[1:].split('/')
				i = s.index(x)
				j = s.index(y)
				t = s[i]
				s[i] = s[j]
				s[j] = t

	print('Part one:', sequence[1])
	print('Part two:', sequence[1000000000 % len(sequence)])

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

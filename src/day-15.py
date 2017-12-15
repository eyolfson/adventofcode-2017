import argparse
import re

def next_a(a):
	a *= 16807
	a %= 2147483647
	return a

def next_b(b):
	b *= 48271
	b %= 2147483647
	return b

def next_a2(a):
	while True:
		a *= 16807
		a %= 2147483647
		if a % 4 == 0:
			break
	return a

def next_b2(b):
	while True:
		b *= 48271
		b %= 2147483647
		if b % 8 == 0:
			break
	return b

def main(args):
	matcher = re.compile(r'Generator (A|B) starts with (\d+)\n$')
	with open(args.path, 'r') as f:
		for line in f:
			m = matcher.match(line)
			if m.group(1) == 'A':
				a = int(m.group(2))
			elif m.group(1) == 'B':
				b = int(m.group(2))
	a2 = a
	b2 = b
	m = 2**16

	count = 0
	for _ in range(40000000):
		a = next_a(a)
		b = next_b(b)
		if (a % m) == (b % m):
			count += 1
	print('Part one:', count)

	count2 = 0
	for _ in range(5000000):
		a2 = next_a2(a2)
		b2 = next_b2(b2)
		if (a2 % m) == (b2 % m):
			count2 += 1
	print('Part two:', count2)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

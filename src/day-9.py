import argparse
import re

class Group:

	def __init__(self, groups):
		self.groups = groups

	def pretty_print(self):
		return '{{{}}}'.format(','.join([x.pp() for x in self.groups]))

	def score(self, current=1):
		s = current
		for group in self.groups:
			s += group.score(current + 1)
		return s

class Parser:

	def __init__(self, data):
		self.data = data
		self.i = 0
		self.non_cancelled = 0

	def peek(self, c):
		return self.data[self.i] == c

	def advance(self):
		self.i += 1

	def expect(self, c):
		assert self.data[self.i] == c, 'expected {}'.format(c)
		self.advance()

	def group(self):
		groups = []
		self.expect('{')
		if self.peek('{'):
			groups.append(self.group())
		elif self.peek('<'):
			self.garbage()
		while self.peek(','):
			self.advance()
			if self.peek('{'):
				groups.append(self.group())
			elif self.peek('<'):
				self.garbage()
		self.expect('}')
		return Group(groups)

	def garbage(self):
		self.expect('<')
		while not self.peek('>'):
			if self.peek('!'):
				self.advance()
				self.advance()
			else:
				self.advance()
				self.non_cancelled += 1
		self.expect('>')

	def parse(self):
		if self.peek('{'):
			return self.group()
		else:
			return None
		assert self.i == len(self.data)

	def get_non_cancelled(self):
		return self.non_cancelled

def main(args):
	with open(args.path, 'r') as f:
		data = f.read().replace('\n', '')
	p = Parser(data)
	g = p.parse()
	assert Group != None, "Did not find group"
	print('Part one:', g.score())
	print('Part two:', p.non_cancelled)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

import argparse
import collections
import math
import itertools

def prime(n):
	return n > 1 and all(n % i for i in itertools.islice(itertools.count(2), int(math.sqrt(n)-1)))

class CPU:
	def __init__(self, insts, a=None):
		self.insts = insts
		self.regs = collections.defaultdict(int)
		if a != None:
			self.regs['a'] = a
		self.pc = 0
		self.num_mul = 0

	def get(self, s):
		try:
			val = int(s)
		except:
			val = self.regs[s]
		return val

	def get_num_mul(self):
		return self.num_mul

	def step(self):
		if self.pc == len(self.insts):
			return False
		inst = self.insts[self.pc]
		op = inst[0]
		if op == 'set':
			self.regs[inst[1]] = self.get(inst[2])
		elif op == 'add':
			self.regs[inst[1]] += self.get(inst[2])
		elif op == 'sub':
			self.regs[inst[1]] -= self.get(inst[2])
		elif op == 'mul':
			self.regs[inst[1]] *= self.get(inst[2])
			self.num_mul += 1
		elif op == 'mod':
			self.regs[inst[1]] %= self.get(inst[2])
		elif op == 'jnz':
			val = self.get(inst[1])
			if val != 0:
				offset = self.get(inst[2])
				self.pc += offset - 1
		else:
			assert False
		self.pc += 1
		return True

def main(args):
	insts = []
	with open(args.path, 'r') as f:
		for line in f:
			insts.append(line.strip().split())

	cpu = CPU(insts)
	while cpu.step():
		pass
	print('Part one:', cpu.get_num_mul())

	cpu = CPU(insts, 1)
	for _ in range(7):
		cpu.step()

	b = cpu.get('b')
	c = cpu.get('c')
	h = 0
	for x in range(b, c + 1, 17):
		if not prime(x):
			h += 1
	print('Part two:', h)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

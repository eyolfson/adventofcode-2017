import argparse
import collections

class CPU:
	def __init__(self, insts, pid=0):
		self.insts = insts
		self.regs = collections.defaultdict(int)
		self.pid = pid
		self.regs['p'] = pid
		self.pc = 0
		self.send_queue = []
		self.recieve_queue = None
		self.last_snd_val = 0
		self.values_sent = 0

	def get(self, s):
		try:
			val = int(s)
		except:
			val = self.regs[s]
		return val

	def get_send_queue(self):
		return self.send_queue

	def set_recieve_queue(self, q):
		self.recieve_queue = q

	def get_last_snd_val(self):
		return self.last_snd_val

	def get_values_sent(self):
		return self.values_sent

	def step(self):
		inst = self.insts[self.pc]
		op = inst[0]
		if op  == 'snd':
			val = self.get(inst[1])
			self.send_queue.append(val)
			self.last_snd_val = val
			self.values_sent += 1
		elif op == 'set':
			self.regs[inst[1]] = self.get(inst[2])
		elif op == 'add':
			self.regs[inst[1]] += self.get(inst[2])
		elif op == 'mul':
			self.regs[inst[1]] *= self.get(inst[2])
		elif op == 'mod':
			self.regs[inst[1]] %= self.get(inst[2])
		elif op == 'jgz':
			val = self.get(inst[1])
			if val > 0:
				offset = self.get(inst[2])
				self.pc += offset - 1
		elif op == 'rcv':
			if self.recieve_queue == None:
				if self.get(inst[1]) != 0:
					return False
				else:
					self.pc += 1
					return True
			if len(self.recieve_queue) > 0:
				self.regs[inst[1]] = self.recieve_queue.pop(0)
			else:
				return False
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
	print('Part one:', cpu.get_last_snd_val())

	cpu0 = CPU(insts, 0)
	cpu1 = CPU(insts, 1)
	cpu0.set_recieve_queue(cpu1.get_send_queue())
	cpu1.set_recieve_queue(cpu0.get_send_queue())
	while cpu0.step() or cpu1.step():
		while cpu0.step():
			pass
		while cpu1.step():
			pass
	print('Part two:', cpu1.get_values_sent())

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

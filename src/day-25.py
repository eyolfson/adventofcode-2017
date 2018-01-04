import argparse
import collections
import re

class Insts:
	def __init__(self):
		self.write = None
		self.move = None
		self.next_state = None

def state_to_index(c):
	return ord(c) - ord('A')

def main(args):
	state_begin_re = re.compile(r'Begin in state ([A-Z])\.\n')
	checksum_steps_re = re.compile(r'Perform a diagnostic checksum after (\d+) steps\.\n')
	in_state_re = re.compile(r'In state ([A-Z]):\n')
	if_value_re = re.compile(r'  If the current value is ([0|1]):\n')
	write_re = re.compile(r'    - Write the value ([0|1])\.\n')
	move_re = re.compile(r'    - Move one slot to the (left|right)\.\n')
	next_state_re = re.compile(r'    - Continue with state ([A-Z])\.\n')

	machine = {}
	with open(args.path, 'r') as f:
		for line in f:
			m = state_begin_re.match(line)
			if m:
				state_current = state_to_index(m.group(1))
				continue
			m = checksum_steps_re.match(line)
			if m:
				checksum_steps = int(m.group(1))
				continue
			m = in_state_re.match(line)
			if m:
				in_state = state_to_index(m.group(1))
				machine[in_state] = {}
				continue
			m = if_value_re.match(line)
			if m:
				if_value = int(m.group(1))
				machine[in_state][if_value] = Insts()
				continue
			m = write_re.match(line)
			if m:
				machine[in_state][if_value].write = int(m.group(1))
				continue
			m = move_re.match(line)
			if m:
				if m.group(1) == 'left':
					machine[in_state][if_value].move = -1
				elif m.group(1) == 'right':
					machine[in_state][if_value].move = 1
				else:
					assert False
				continue
			m = next_state_re.match(line)
			if m:
				machine[in_state][if_value].next_state = state_to_index(m.group(1))
				continue

	tape = [0 for _ in range(checksum_steps + 1)]
	i = 0
	num_ones = 0
	for _ in range(checksum_steps):
		value_current = tape[i]
		insts = machine[state_current][value_current]

		tape[i] = insts.write
		i += insts.move
		state_current = insts.next_state

		if value_current == 0 and insts.write == 1:
			num_ones += 1
		elif value_current == 1 and insts.write == 0:
			num_ones -= 1

	print('Part one:', num_ones)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)

def main():
	steps = 376

	s = [0]
	i = 0
	for v in range(1, 2018):
		i = (i + steps) % len(s)
		i += 1
		s = s[:i] + [v] + s[i:]
	print('Part one:', s[s.index(2017) + 1])

	ans = 0
	i = 0
	for v in range(1, 50000001):
		i = (i + steps) % (v)
		if (i == 0):
			ans = v
		i += 1
	print('Part two:', ans)

if __name__ == '__main__':
	main()

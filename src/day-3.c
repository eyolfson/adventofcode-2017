#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define LENGTH 31

static const int input = 265149;

void part_one()
{
	int layer = 0;
	int root = 0;
	int bottom_right = 1;
	while (true) {
		if (input <= bottom_right)
			break;

		layer += 1;
		root = layer * 2 + 1;
		bottom_right = root * root;
	}

	int max_to_middle = (root - 1) / 2;
	int current_middle = bottom_right - max_to_middle;

	while (true) {
		int distance_to_middle = abs(input - current_middle);
		if (distance_to_middle > max_to_middle) {
			current_middle -= (max_to_middle * 2);
			continue;
		}
		printf("Part one: %d\n", layer + distance_to_middle);
		break;
	}
}

void part_two()
{
	int data[LENGTH][LENGTH] = {0};
	int x = ((LENGTH - 1) / 2) - 1;
	int y = x;

	data[x][y] = 1;

	int direction = 1;
	int steps = 1;

	bool found = false;
	while (!found) {
		for (int step = 0; step < steps; ++step) {
			switch (direction) {
			case 1:
				++x;
				break;
			case 2:
				++y;
				break;
			case 3:
				--x;
				break;
			case 4:
				--y;
				break;
			}

			int sum = 0;
			for (int i = -1; i < 2; ++i) {
				for (int j = -1; j < 2; ++j) {
					if (i == 0 && j == 0)
						continue;
					sum += data[x + i][y + j];
				}
			}
			data[x][y] = sum;
			if (sum > input) {
				printf("Part two: %d\n", sum);
				found = true;
				break;
			}
		}

		if (direction == 2 || direction == 4) {
			++steps;
		}
		++direction;
		if (direction == 5)
			direction = 1;
	}
}

int main()
{
	part_one();
	part_two();

	return 0;
}

import sys
sys.path.insert(0, '/Users/andreasaurlien/github/advent-of-code-2021/src')

import numpy as np
from functions import get_file_numbers
from functions import debug
from day_1.task_1 import count_next_number_greater


def sum_window(first_numbers, window):
    sum = np.zeros_like(first_numbers)
    for i in range(window):
        sum += np.roll(first_numbers, -i)
    return sum[:-window+1]


def main():
    numbers = get_file_numbers('./test-data/task_2.txt')
    print(count_next_number_greater(sum_window(numbers, 3)))


if __name__ == '__main__':
    main()

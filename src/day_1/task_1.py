import sys
sys.path.insert(0, '/Users/andreasaurlien/github/advent-of-code-2021/src')

import numpy as np
from functions import get_file_numbers


def count_next_number_greater(numbers):
    next_numbers = np.roll(np.copy(numbers), -1)
    diff = numbers[:-1] - next_numbers[:-1]
    return np.count_nonzero(diff < 0)


def main():
    numbers = get_file_numbers('./test-data/task_1_example.txt')
    answer = count_next_number_greater(numbers)
    print(answer)

if __name__ == '__main__':
    main()

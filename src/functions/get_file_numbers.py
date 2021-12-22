def get_file_numbers(file):
    with open(file) as f:
        return [int(n) for n in f]

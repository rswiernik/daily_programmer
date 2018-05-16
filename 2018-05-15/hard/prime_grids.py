import os
from math import sqrt

def is_prime(n):
    if n == "0":
        return False
    if n == "1":
        return True
    if n in [2,3]:
        return True
    if (n%2) == 0:
        return False
    for i in xrange(3, int(sqrt(n)), 2):
        if (n%i) == 0:
            return False
    return True

class Grid(object):
    def __init__(self, filename, size):
        self.filename = filename
        self.size = size
        self.grid = []

    def add_line(self, line):
        self.grid.append(line)

    def _yield_next_prime_pair(self):
        # rows
        for row in self.grid:
            n_str = ''.join(row)
            yield [int(n_str), int(n_str[::-1])]
        # columns
        for x in range(0, self.size):
            column = []
            for row in self.grid:
                column.append(self.grid[x])
            n_str = ''.join(column)
            yield [int(n_str), int(n_str[::-1])]
        # diagonals
        for row_n in range(0, self.size):
            for col_n in range(0, self.size):
                if (row_n != 0) or (row_n != self.size) or \
                    (col_n != 0) or (col_n != self.size):
                    continue

                diag = []
                col_cursor = col_n
                row_cursor = row_n
                while (col_cursor >= 0) and (row_cursor < self.size):
                    diag.append(self.grid[col_n][row_n])
                    col_cursor -= 1
                    row_cursor += 1
                n_str = ''.join(diag)
                yield [int(n_str), int(n_str[::-1])]

    def primes(self):
        primes = []
        for pair in self._yield_next_prime_pair():
            for n in pair:
                if is_prime(n):
                    primes.append(n)
        return primes

    def __str__(self):
        return ("{}, {}".format(self.filename, str(self.size)))

def find_primes(filename):
    grids = []

    with open(filename, 'r') as f:
        current_grid = None
        for line in f:
            if not current_grid:
                size = int(line.strip())
                current_grid = Grid(filename, size)
            elif line == "\n" or line == None:
                grids.append(current_grid)
                current_grid = None
            else:
                current_grid.add_line(line.strip())
        if current_grid != None:
            grids.append(current_grid)

    for grid in grids:
        print grid.primes()

if __name__ == "__main__":
    dir_contents = os.listdir("./")
    input_files = []
    for entry in dir_contents:
        if not os.path.isfile(entry):
            continue
        elif entry.endswith(".in"):
            input_files.append(entry)

    for item in input_files:
        find_primes(item)



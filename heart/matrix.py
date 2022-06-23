import numpy as np


class Matrix:
    def __init__(self, size: int):
        self.matrix = np.zeros((size, size), dtype=int)

    def _mirror_matrix(self):
        output = list(self.matrix[::-1])
        output.extend(self.matrix[1:])
        return output

    def draw_half_heart(self):
        matrix_size = len(self.matrix)
        heart_size = matrix_size - 1
        one_third = int(matrix_size * 0.33)

        for row in self.matrix:
            parallel_lines = [abs(heart_size - one_third * 2), heart_size]
            row[parallel_lines[0]] = 1
            row[parallel_lines[1]] = 1

            heart_size -= 1
            if parallel_lines[0] == parallel_lines[1]:
                break

    def make_heart(self):
        self.matrix = np.asarray(self._mirror_matrix()).transpose()

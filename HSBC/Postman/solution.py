import numpy as np
class Solution:

    def find_path(self, lawn):
        # Your code goes here
        lines = np.array(list(map(list,lawn.splitlines()[1:])))
        if lines.size == 0:
            return list(range(len(lawn)))
        matrix = np.where(lines == 'D', 1, 0)
        paths = []
        for j in range(matrix.shape[1]):
            if not np.any(matrix[:,j]):
                paths.append(j)
        return paths if paths else [-1]
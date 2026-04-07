import numpy as np
from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku = np.array(board)

        for i in range(0, 9):
            counter = Counter(sudoku[:, i])
            del counter["."]
            if len(counter.values()) > 0:
                if max(counter.values()) > 1:
                    return False
        

        for row in sudoku:
            counter = Counter(row)
            del counter['.']
            if len(counter.values()) > 0:
                if max(counter.values()) > 1:
                    return False

        for n_col in range(1, 4):
            for n_row in range(1, 4):
                counter = Counter(sudoku[(n_col - 1)*3:n_col*3, (n_row-1)*3:(n_row*3)].flatten())
                del counter["."]
                if len(counter.values()) > 0:
                    if max(counter.values()) > 1:
                        return False

        return True
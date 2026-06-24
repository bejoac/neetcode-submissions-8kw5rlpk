class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row_len = len(matrix[0])

        transpose = [[] for _ in range(row_len)]

        for row in matrix:
            for i, element in enumerate(row):
                transpose[i].append(element)

        return transpose

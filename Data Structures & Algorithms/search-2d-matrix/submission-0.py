class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_matrix = []

        for row in matrix:
            flat_matrix.extend(row)

        L, R = 0, len(flat_matrix) - 1
        mid = (R - L) // 2

        while L <= R:
            if target < flat_matrix[mid]:
                R = mid - 1
                mid = L + (R - L) // 2
            elif target == flat_matrix[mid]:
                return True
            elif target > flat_matrix[mid]:
                L = mid + 1
                mid = R - (R - L) // 2

        return False
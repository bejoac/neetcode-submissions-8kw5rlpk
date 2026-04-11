class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        T, B = 0, len(matrix) - 1
        mid = (B - T) // 2
        found_row = False

        while T <= B:
            if target < matrix[mid][0]:
                B = mid - 1
                mid = T + (B - T) // 2
            elif target >= matrix[mid][0] and target <= matrix[mid][-1]:
                found_row = True
                row_index = mid
                break
            elif target > matrix[mid][-1]:
                T = mid + 1
                mid = B - (B - T) // 2

        if not found_row:
            return False

        row = matrix[row_index]
        L, R = 0, len(row) - 1
        mid = (R - L) // 2

        while L <= R:
            if target < row[mid]:
                R = mid - 1
                mid = L + (R - L) // 2
            elif target == row[mid]:
                return True
            elif target > row[mid]:
                L = mid + 1
                mid = R - (R - L) // 2

        return False
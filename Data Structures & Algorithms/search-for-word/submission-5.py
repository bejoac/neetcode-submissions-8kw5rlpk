class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        H, W = len(board) - 1, len(board[0]) - 1

        def search(i, j, curr, visited):
            if curr == word:
                return True
            if (i, j) in visited:
                return False
            if i > H or j > W or i < 0 or j < 0:
                return False
            if board[i][j] not in word:
                return False
            if curr != word[:len(curr)]:
                return False

            curr = curr + board[i][j]
            visited.append((i, j))
            result = search(i + 1, j, curr, visited) or search(i, j + 1, curr, visited) or search(i - 1, j, curr, visited) or search(i, j - 1, curr, visited)
            visited.remove((i, j))
            return result 
            
        for i in range(H + 1):
            for j in range(W + 1):
                if board[i][j] == word[0]:
                    found = search(i, j, "", [])
                    if found:
                        return True

        return False
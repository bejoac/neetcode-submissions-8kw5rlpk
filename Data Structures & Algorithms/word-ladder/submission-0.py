class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = [(beginWord, 1)]
        visited = [beginWord]

        while queue:
            word, level = queue.pop(0)

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i+1:]

                    if new_word not in visited and new_word != word and new_word in wordList:
                        if new_word == endWord:
                            return level + 1

                        queue.append((new_word, level + 1))
                        visited.append(new_word)

        return 0 
                        
                        
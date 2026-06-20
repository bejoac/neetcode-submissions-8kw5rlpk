class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {}

        for i, c in enumerate(order):
            mapping[c] = i

        def compare(word):
            return [mapping[c] for c in word]

        sorted_words = sorted(words, key=compare)

        return sorted_words == words
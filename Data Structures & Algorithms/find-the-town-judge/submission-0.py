class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        candidates = []
        people = []

        for candidate in range(1, n + 1):
            candidates.append(candidate)

        for trust_relation in trust:
            if trust_relation[0] in candidates:
                people.append(trust_relation[0])
                candidates.remove(trust_relation[0])

        if not candidates or len(candidates) > 1:
            return -1

        town_judge = candidates[0]

        for person in people:
            if [person, town_judge] not in trust:
                return -1 
                
        return town_judge
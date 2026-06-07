class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort() # O(logn)
        q_hand = deque(hand)
        group = []
        duplicates = deque()

        while q_hand:
            while len(group) < groupSize:
                if not q_hand: # That feels like cheating
                    return False

                cur = q_hand.popleft() 

                if not group:
                    group.append(cur)
                    continue
                
                if group[-1] == cur: # Duplicates
                    duplicates.appendleft(cur)
                    continue
                
                if abs(cur - group[-1]) != 1: # Invalid
                    return False
                else:
                    group.append(cur) # Valid
                    
            group = []
            for duplicate in duplicates:
                q_hand.appendleft(duplicate)
            duplicates = deque()

        return True
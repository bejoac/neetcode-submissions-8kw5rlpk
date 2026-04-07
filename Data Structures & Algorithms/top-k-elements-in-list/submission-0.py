class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            if num in freqs:
                freqs[num] +=1
            else:
                freqs[num] =1
        
        freqs_sorted = {k: v for k, v in sorted(freqs.items(), key=lambda item: item[1])}
        return [elem for elem in freqs_sorted.keys()][-k:] 

        
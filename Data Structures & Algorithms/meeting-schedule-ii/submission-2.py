"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1
        
        min_heap = []
        heapq.heapify(min_heap)
    
        for interval in intervals:
            heapq.heappush(min_heap, (interval.start, interval.end))

        rooms = [[heapq.heappop(min_heap)]]

        while min_heap:
            cur = heapq.heappop(min_heap)
            
            for room in rooms:
                if cur[0] >= room[-1][1]:
                    room.append(cur)
                    break
            else:
                rooms.append([cur])

        return len(rooms)
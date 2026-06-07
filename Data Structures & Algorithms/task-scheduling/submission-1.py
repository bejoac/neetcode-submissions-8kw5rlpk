class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-cnt for cnt in counter.values()]
        heapq.heapify(max_heap)

        # Schedules when we add to the max_heap
        dq = deque() # cnt, scheduled time
        time = 0

        while dq or max_heap:
            time += 1
            
            if max_heap:
                cur_task_cnt = 1 + heapq.heappop(max_heap)
                if cur_task_cnt:
                    dq.appendleft((cur_task_cnt, time + n))
            
            if dq and time == dq[-1][1]:
                cur_task_cnt, _ = dq.pop()
                heapq.heappush(max_heap, cur_task_cnt)

        return time
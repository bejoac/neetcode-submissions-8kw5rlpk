class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        # Intersection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # At this point we know slow = fast
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow2 == slow:
                return slow2

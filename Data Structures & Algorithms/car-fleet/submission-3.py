class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n_cars = len(position)

        position_and_speed = list(zip(position, speed))
        position_and_speed.sort(reverse=True)

        stack = []

        for p, s in position_and_speed:
            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
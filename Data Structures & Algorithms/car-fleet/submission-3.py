class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []

        for pos, v in sorted(zip(position, speed)):
            stack.append((target - pos) / v)

        temp = 0
        diff_car_fleets = 0
        for i in reversed(stack):
            if temp < i:
                temp = i
                diff_car_fleets += 1
            else:
                continue

        return diff_car_fleets
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        car = [(position[i], speed[i]) for i in range(n)]
        car = sorted(car, key=lambda x: x[0])

        stack = []

        for i in range(n - 1, -1, -1):
            time = (target - car[i][0])/car[i][1]
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)

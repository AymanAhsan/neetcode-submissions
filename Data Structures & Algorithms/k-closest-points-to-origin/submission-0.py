class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_arr = []
        res = []
        for point in points:
            distance = math.sqrt((point[0] - 0) ** 2 + (point[1] - 0) ** 2)
            distance_arr.append((distance, point))
        heapq.heapify(distance_arr)
        for i in range(k):
            _, point_data = heapq.heappop(distance_arr)
            res.append(point_data)
        return res

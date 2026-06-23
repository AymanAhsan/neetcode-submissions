class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = []
        max_heap = [(-count, key) for key, count in counts.items()]
        heapq.heapify(max_heap)

        for i in range(k):
            res.append((heapq.heappop(max_heap))[1])
        return res


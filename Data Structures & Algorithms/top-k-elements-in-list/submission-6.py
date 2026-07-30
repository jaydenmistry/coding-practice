class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # O(n)
        for i, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1

        # O(n)
        minHeap = []
        for (key, val) in freq.items():
            heapq.heappush(minHeap, (val, key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        # O(n)
        result = []
        for i in range(k):
            result.append(heapq.heappop(minHeap)[1])

        return result

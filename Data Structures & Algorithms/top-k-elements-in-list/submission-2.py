class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        # O(n)
        for i, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1
        
        # O(n)
        pairs = []
        for i, (key, val) in enumerate(freq.items()):
            pairs.append([val, key])
        
        # O(nlog(n))
        pairs = sorted(pairs)

        # O(n)
        result = []
        for i in range(k):
            result.append(pairs.pop()[1])

        return result
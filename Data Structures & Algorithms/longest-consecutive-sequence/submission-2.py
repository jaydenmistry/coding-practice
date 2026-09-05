class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        seen = set()
        maxCount = 0

        for num in numSet:
            if (num - 1) not in numSet:
                count = 1
                current_num = num
                
                while (current_num + 1) in numSet:
                    count += 1
                    current_num += 1
                
                maxCount = max(maxCount, count)

        return maxCount
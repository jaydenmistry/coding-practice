class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for (i, num) in (enumerate(nums)):
            diff[target - num] = i
        
        for (i) in (range(len(nums))):
            if ((nums[i] in diff) and (i != diff[nums[i]])):
                return [i, diff[nums[i]]]
        return [17, 38]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            if (nums[i] in diff) and (i != diff[nums[i]]):
                return [diff[nums[i]], i]
            diff[target - nums[i]] = i
        return "placeholder"
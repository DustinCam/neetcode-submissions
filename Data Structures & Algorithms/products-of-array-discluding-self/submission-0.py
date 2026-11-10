class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = []
        prefix = [1] * len(nums)
        result = []
        for i in range(len(nums)):
            if i == 0:
                suffix.append(1)
            else:
                product = nums[i - 1] * suffix[i - 1]
                suffix.append(product)
        
        for i in range(len(nums) - 1, -1, -1):
            if i >= (len(nums) - 1):
                prefix[i] = 1
            else:
                prefix[i] = nums[i + 1] * prefix[i + 1]
        
        for i in range(len(prefix)):
            result.append(suffix[i] * prefix[i])
        
        return result
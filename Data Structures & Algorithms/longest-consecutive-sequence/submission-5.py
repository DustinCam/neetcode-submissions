class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        count = 0
        longest = 0

        for i in range(len(sorted_nums)):
            if i == 0:
                count += 1
                continue

            if (sorted_nums[i] - sorted_nums[i - 1]) == 1:
                count += 1
                if longest < count:
                    longest = count
            elif (sorted_nums[i] - sorted_nums[i - 1]) > 1:
                if longest < count:
                    longest = count
                count = 1

        if longest < count:
            longest = count
        return longest
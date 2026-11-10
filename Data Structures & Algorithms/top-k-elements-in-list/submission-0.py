class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        
        def get_frequency(item):
            return item[1]

        sorted_items = sorted(seen.items(), key=get_frequency, reverse=True)

        sorted_freq = dict(sorted_items)

        keys = list(sorted_freq.keys())

        return keys[:k]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            key = tuple(sorted(word))
            if key not in group:
                group[key] = [word]
            else:
                group[key].append(word)
        return list(group.values())
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in sdict:
                sdict[s[i]] = 1
            else:
                sdict[s[i]] += 1

            if t[i] not in tdict:
                tdict[t[i]] = 1
            else:
                tdict[t[i]] += 1
        
        ssort = dict(sorted(sdict.items(), key=lambda item: item[1]))
        tsort = dict(sorted(tdict.items(), key=lambda item: item[1]))

        return sdict == tdict
            

        
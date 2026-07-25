class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd, td = {}, {}
        if len(s) == len(t):
            for i in range(len(s)):
                sd[s[i]] = sd.get(s[i], 0) + 1
                td[t[i]] = td.get(t[i], 0) + 1
            if sd == td:
                return True
        return False
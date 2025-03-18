class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        maximum = 0
        res = set()
        while j < len(s):
            if s[j] not in res:
                res.add(s[j])
                j += 1
                maximum = max(maximum, len(res))
            else:
                res.remove(s[i])
                i += 1
        return maximum

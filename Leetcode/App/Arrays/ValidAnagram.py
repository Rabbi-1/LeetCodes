class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))
        return sorted_s == sorted_t

    def isAnagram2(self, s: str, t: str) -> bool:
        count = [0] * 26

        for i in s:
            count[ord(i) - ord('a')] += 1
        for i in t:
            count[ord(i) - ord('a')] -= 1
        for val in count:
            if val != 0:
                return False
        return True
#Leetcode 242
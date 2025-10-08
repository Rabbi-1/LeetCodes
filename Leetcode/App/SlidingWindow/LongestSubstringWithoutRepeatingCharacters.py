class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        res = set()
        left = right = 0
        while right < len(s):
            while s[right] in res:
                res.remove(s[left])
                left += 1
            max_len = max(max_len, right - left + 1)
            res.add(s[right])
            right += 1
        return max_len

#Time complexity: O(n) b/c we traverse the string linearly with two pointers
#Space complexity: O(m) b/c we use a hash set to store unique character where m represents the total number of
# unique character within the string.
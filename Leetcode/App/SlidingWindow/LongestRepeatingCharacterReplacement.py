class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        max_count = 0
        left = 0
        max_length = 0
        for right in range(len(s)):
            inx = ord(s[right]) - ord('A')
            count[inx] += 1
            max_count = max(max_count, count[inx])
            if (right - left + 1) - max_count > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
#Leetcode 424
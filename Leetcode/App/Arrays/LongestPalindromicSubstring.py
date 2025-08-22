def longestPalindrome(self, s: str) -> str:
    if len(s) <= 1:
        return s

    def expandCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    max_str = s[0]

    for i in range(len(s) - 1):
        odd = expandCenter(i, i)
        even = expandCenter(i, i + 1)

        if len(odd) > len(max_str): max_str = odd
        if len(even) > len(max_str): max_str = even

    return max_str

#Longest Palindromic Substring
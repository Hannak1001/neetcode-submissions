class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLen = 0
        substring = set()

        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[left])
                left += 1
            substring.add(s[r])
            maxLen = max(maxLen, len(substring))
        return maxLen

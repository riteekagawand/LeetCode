class Solution(object):
    def longestPalindrome(self, s):
        max_len = 0
        longest = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    if max_len < len(substring):
                        max_len = len(substring)
                        longest = substring
        return longest

        """
        :type s: str
        :rtype: str
        """
        
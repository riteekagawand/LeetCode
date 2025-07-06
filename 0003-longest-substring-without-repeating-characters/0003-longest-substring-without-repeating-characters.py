class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len =0
        for i in range(len(s)):
            current_len = 0
            s2 = set()
            for j in range (i, len(s)):
                if s[j] in s2 :
                    break
                else:
                    s2.add(s[j])
                    current_len +=1
            max_len = max(max_len, current_len)

        return max_len


        """
        :type s: str
        :rtype: int
        """
        
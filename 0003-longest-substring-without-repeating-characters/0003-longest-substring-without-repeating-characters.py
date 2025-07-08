class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            s1=set()
            curr=0
            for j in range(i,len(s)):
                if s[j] in s1:
                    break
                else:
                    s1.add(s[j])
                    curr+=1
            max_len=max(max_len,curr)
        return max_len
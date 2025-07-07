class Solution(object):
    def countSubstrings(self, s):
        count = 0
        def expandCenter(left,right):
            nonlocal count
            while left>=0 and right < len(s) and s[left] == s[right]:
                count+=1
                left-=1
                right+=1
       

        for i in range (len(s)):
            expandCenter(i,i)
            expandCenter(i,i+1)

        return count

        """
        :type s: str
        :rtype: int
        """
        
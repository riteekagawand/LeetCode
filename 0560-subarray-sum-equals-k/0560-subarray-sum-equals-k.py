class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        curr_sum = 0
        pre = {0:1}

        for i in nums:
            curr_sum += i
            if curr_sum -k in pre:
                count += pre[curr_sum -k]
            pre[curr_sum] = pre.get(curr_sum, 0)+1
        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
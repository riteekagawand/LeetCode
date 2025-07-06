class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        sorted_nums = sorted(set(nums))
        longest = 1
        streak = 1
        for i in range (1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1]+1:
                streak += 1

            else:
                longest = max(longest, streak)
                streak = 1

        return max(longest,streak)


        # result = []
        # result.append(sorted_nums[0])
        # for i in range (len(sorted_nums)):
        #         if sorted_nums[i] == sorted_nums[i-1]+1:
        #             result.append(sorted_nums[i])
        # return len(result)

       

        """
        :type nums: List[int]
        :rtype: int
        """
        
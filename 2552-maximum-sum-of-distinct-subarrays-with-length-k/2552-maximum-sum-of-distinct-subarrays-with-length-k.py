class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        s1 = set()
        curr_sum = 0
        max_sum =0
        for right in range(len(nums)):
            while nums[right] in s1:
                s1.remove(nums[left])
                curr_sum -= nums[left]
                left +=1
            s1.add(nums[right])
            curr_sum += nums[right]

            if right - left +1 == k:
                max_sum = max(max_sum,curr_sum)
                s1.remove(nums[left])
                curr_sum -= nums[left]
                left+=1
        return max_sum
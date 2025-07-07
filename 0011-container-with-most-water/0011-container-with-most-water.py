class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxarea=0
        # h = max(left,right)
        while left < right:
            width = right - left
            high = min(height[left],height[right])
            area = width * high
            maxarea = max(area,maxarea)
            if height[left] > height[right]:
                right-=1   
            else:
                left+=1
        return maxarea     
        # max_area = 0
        # for i in range (len(height)):
        #     # j = len(height)-1
        #     for j in range (i+1,len(height)):
        #         width = j-i
        #         h = min(height[i],height[j])
        #         area = width *h
        #         max_area = max(area,max_area)
        # return max_area


        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxReturn = 0
        flag = 0

        while left <= right:
            h = min(heights[right], heights[left])
            w = right - left

            alan = h * w

            if maxReturn < alan:
                maxReturn = alan
            
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
                

        return maxReturn

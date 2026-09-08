class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        maxReturn = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                
                temp = h * w 

                if maxReturn < temp:
                    maxReturn = temp

            stack.append(i)
        
        return maxReturn


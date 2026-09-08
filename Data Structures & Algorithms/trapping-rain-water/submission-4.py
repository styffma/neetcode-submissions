class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0
        total = 0
        while left < right:
            if left_max < height[left]:
                left_max = height[left]
            if right_max < height[right]:
                right_max = height[right]
            
            if left_max < right_max:
                left+=1
                temp = left_max - height[left]
                if temp>0:
                    total += temp 
            else:
                right-=1
                temp2 = right_max - height[right]
                if temp2>0:
                    total += temp2 
        return total
        

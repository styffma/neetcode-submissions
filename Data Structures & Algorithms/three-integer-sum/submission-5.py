class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left_j = i + 1
            right_k = len(nums)-1
            
            while left_j < right_k:
                temp = nums[left_j] + nums[right_k]

                if temp < -nums[i]:
                    left_j+=1
                elif temp > -nums[i]:
                    right_k-=1
                else:
                    output.append([nums[i], nums[left_j], nums[right_k]])
                    right_k-=1
                    left_j+=1

                    while left_j < right_k and nums[left_j] == nums[left_j-1]:
                        left_j+=1

        return output
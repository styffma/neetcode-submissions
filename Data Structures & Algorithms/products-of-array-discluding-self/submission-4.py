class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        if not any(nums):
            total = 0
        else:
            total = 1
        hasZero = 0
        for num in nums:
            if num == 0:
                hasZero += 1
                continue
            total *= num
        
        for num in nums:
            if hasZero > 1:
                output.append(0)
            elif hasZero == 1 and num == 0:
                 output.append(total)
            elif hasZero == 1 and num != 0:
                output.append(0)
            else:
                output.append(total // num)
        return output
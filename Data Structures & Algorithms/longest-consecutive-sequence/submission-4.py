class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(nums)

        temp_con = 1
        max_con = 0

        for i in range(len(sorted_nums)-1):
            if sorted_nums[i] + 1 == sorted_nums[i+1]:
                temp_con+=1
            elif sorted_nums[i] == sorted_nums[i+1]:
                continue
            else:
                if max_con < temp_con:
                    max_con = temp_con
                temp_con = 1

        if max_con < temp_con:
            max_con = temp_con

        return max_con
            
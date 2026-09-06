class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_con = 0

        for num in set_nums:
            if num-1 not in set_nums:
                
                cur_num = num
                temp_con = 1

                while cur_num + 1 in set_nums:
                    cur_num+=1
                    temp_con+=1

                max_con = max(max_con, temp_con)
        
        return max_con

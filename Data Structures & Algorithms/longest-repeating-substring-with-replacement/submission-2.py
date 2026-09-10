class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_length = 0
        left = 0
        temp_dict = {}
        main_char = 0 # en çok geçen harfin kaç kere geçtiği

        for right in range(len(s)):
            
            temp_dict[s[right]] = temp_dict.get(s[right], 0) + 1
            main_char = max(main_char, temp_dict[s[right]])

            while k < right-left+1 - main_char:
                temp_dict[s[left]] -= 1
                left+=1

            max_length = max(max_length, right-left+1)

        return max_length        
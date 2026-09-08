class Solution:
    def isPalindrome(self, s: str) -> bool:
        metin = "".join(i for i in s if i.isalnum()).lower()

        left_index = 0
        right_index = len(metin) -1

        while left_index < right_index:
            if metin[left_index] == metin[right_index]:
                left_index+=1
                right_index-=1
            else:
                return False
        
        return True

        
        
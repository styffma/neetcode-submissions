class Solution:
    def isPalindrome(self, s: str) -> bool:
        metin = "".join(i for i in s if i.isalnum()).lower()

        return metin[::-1] == metin
        
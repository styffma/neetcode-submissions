class Solution:
    def isPalindrome(self, s: str) -> bool:
        metin = "".join(i for i in s if i.isalnum()).lower()
        for x, y in zip(metin, reversed(metin)):
            if x == y:
                continue
            else:
                return False

        return True
        
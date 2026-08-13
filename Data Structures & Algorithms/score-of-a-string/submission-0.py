class Solution:
    def scoreOfString(self, s: str) -> int:
        toplam = 0
        index_s = 1
        while index_s != len(s):
            toplam += abs(ord(s[index_s]) - ord(s[index_s-1]))
            index_s+=1

        return toplam

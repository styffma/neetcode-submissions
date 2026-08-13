class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        dizi = s.rsplit(" ")
        index_s = -1
        print(dizi)
        while True:
            if dizi[index_s]=="" or dizi[index_s].isspace():
                index_s-=1
            else:
                word = dizi[index_s].replace(" ", "")
                return len(word)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            l.append(word1[i])
            i+=1
            l.append(word2[j])
            j+=1
        
        l.append(word1[i:])
        l.append(word2[j:])
        
        return "".join(l)
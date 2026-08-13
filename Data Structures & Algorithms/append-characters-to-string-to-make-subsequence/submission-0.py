class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        index_s=0
        index_t=0

        while index_s != len(s) and index_t != len(t):
            if s[index_s] == t[index_t]:
                index_s+=1
                index_t+=1
            else:
                index_s+=1
    
        return len(t) - index_t
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:        
        len_s = len(s)
        len_t = len(t)
        index_s = 0
        index_t = 0

        if len_s == 0 :
            return True

        for i in range(len_t):
            if len_s == index_s:
                break
            if s[index_s] == t[index_t]:
                index_s+=1
                index_t+=1
            else:
                index_t+=1
        
        return index_s == len_s


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        for left in range(len(s2)):
            if s2[left] in s1:
                if sorted(s2[left:left+len(s1)]) == sorted(s1):
                    return True
        return False
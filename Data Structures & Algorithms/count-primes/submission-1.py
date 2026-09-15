class Solution:

    def countPrimes(self, n: int) -> int:
        
        liste = [False] * n
        count = 0
        for num in range(2,n):
            if not liste[num]:
                count+=1
                for i in range(num*num, n, num):
                    liste[i] = True 
        
        return count
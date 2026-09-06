class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                cikarilan_sayi = stack.pop()
                output[cikarilan_sayi] = i - cikarilan_sayi
            
            stack.append(i)
        
        return output
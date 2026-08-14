class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dizi = [[1] * x for x in range(1, numRows+1)]
        
        for i in range(2,numRows):
            for j in range(1,len(dizi[i])-1):
                dizi[i][j] = dizi[i-1][j] + dizi[i-1][j-1]
        return dizi
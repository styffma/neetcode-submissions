class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        try:
            while True:
                for i in range(len(strs)):
                    if strs[i][count] == strs[i-1][count]:
                        pass
                    else:
                        return strs[0][:count]
                count+=1

        except Exception:
            return strs[0][:count]
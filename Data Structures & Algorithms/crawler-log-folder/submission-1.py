class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for item in logs:
            if item == "../":
                if depth != 0:
                    depth-=1
            elif item == "./":
                continue
            else:
                depth+=1
        
        return depth
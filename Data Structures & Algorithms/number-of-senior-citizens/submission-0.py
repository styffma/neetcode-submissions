class Solution:
    def countSeniors(self, details: List[str]) -> int:
        index_d = 0
        total = 0
        while index_d != len(details):
            if int(details[index_d][11:13]) > 60:
                total+=1
            index_d+=1
        return total

        # 11-13
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return_list = []
        for key, value in c.most_common(k):
            return_list.append(key)
        
        return return_list
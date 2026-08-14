class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sozluk = collections.defaultdict(list)
        for i in strs:
            sozluk["".join(sorted(i))].append(i)
        
        return list(sozluk.values())
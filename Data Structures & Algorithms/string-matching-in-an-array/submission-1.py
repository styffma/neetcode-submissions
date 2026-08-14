class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        dizi = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    pass
                elif words[i] in words[j]:
                    if words[i] in dizi:
                        pass
                    else:
                        dizi.append(words[i])
                else:
                    pass
        return dizi
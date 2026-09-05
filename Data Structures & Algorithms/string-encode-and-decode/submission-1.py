class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string = encoded_string + f"{len(s)}#{s}"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        i = 0
        temp = ""
        decoded_strs = []
        while i < len(s):
            while s[i] != "#":
                temp += "".join(s[i])
                i+=1
            i+=1
            temp_int = int(temp)
            decoded_strs.append(s[i:i+temp_int])
            i+=temp_int
            temp = ""
        return decoded_strs
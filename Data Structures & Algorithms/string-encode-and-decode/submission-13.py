class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""
        for strng in strs:
            encoded += (str(len(strng)) + '_' + strng)

        return encoded

    def decode(self, s: str) -> List[str]:
        
        result = []
        start = 0
        i = 0
        while i < len(s):
            if s[i] == '_' and len(s) >= 2:
                length = int(s[start:i])
                result.append(s[(i + 1):(i + 1 + length)])
                i += length
                start = i + 1
            i += 1

        return result
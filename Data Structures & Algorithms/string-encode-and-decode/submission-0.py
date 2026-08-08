class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""
        for i, strng in enumerate(strs):
            encoded += strng + "&#"

        return encoded

    def decode(self, s: str) -> List[str]:
        
        print(s)
        result = []
        start = 0
        for i in range(len(s)):
            if s[i] == '&' and s[i + 1] == '#':
                result.append(s[start:i])
                start = i + 2

        print(result)
        return result
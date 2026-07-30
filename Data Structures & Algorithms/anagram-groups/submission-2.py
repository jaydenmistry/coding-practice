class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {} # Hashmap

        for i, str in enumerate(strs):
            count = [0] * 26 # Hash table of char counts for hashmap key
            for i, char in enumerate(str):
                count[ord(char) - ord('a')] += 1
            words.setdefault(tuple(count), []).append(str)
        
        return list(words.values())
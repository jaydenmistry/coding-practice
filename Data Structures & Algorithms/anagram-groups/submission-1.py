class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words, output = [], []
        for i, str in enumerate(strs):
            dict = {}
            for char in str:
                dict[char] = dict.get(char, 0) + 1
            words.append(dict)
        
        done = [False] * len(strs)
        for i, dict in enumerate(words):
            if done[i] == False:
                tempList = []
                tempList.append(strs[i])
                for j, dict2 in enumerate(words):
                    if dict == dict2 and i != j and done[i] == False and done[j] == False:
                        tempList.append(strs[j])
                        done[j] = True
                done[i] = True
                output.append(tempList)
        return output
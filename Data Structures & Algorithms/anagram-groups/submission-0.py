class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = 0
        nested_map = {}
        ret = []
        for i in range(len(strs)):
            word_map = {}
            for c in strs[i]:
                if c in word_map:
                    word_map[c] += 1
                else:
                    word_map[c] = 1
            tup = tuple(sorted(word_map.items()))
            if tup in nested_map:
                ret[nested_map[tup]].append(strs[i])
            else:
                nested_map[tup] = count
                ret.append([])
                ret[count].append(strs[i])
                count += 1
        return ret

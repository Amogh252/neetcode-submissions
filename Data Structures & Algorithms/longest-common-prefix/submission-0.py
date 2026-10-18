class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        while True:
            if len(strs[0]) == count:
                return strs[0][:count]
            for s in strs:
                if count == len(s):
                    return strs[0][0:count]
                if s[count] != strs[0][count]:
                    return strs[0][:count]
            count += 1

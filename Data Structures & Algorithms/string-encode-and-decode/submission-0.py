class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        parts = []
        for s in strs:
            parts.append(str(len(s)) + "#" + s)
        return "".join(parts)
    def decode(self, s: str) -> List[str]:
        ret = []
        num = 0
        num_str = ""
        i = 0
        while i < (len(s)):
            if(s[i:i+1] == "#"):
                num = int(num_str)
                ret.append(s[i+1:i+1+num])
                num_str = ""
                i += num
            else:
                num_str += s[i]
            i += 1
        return ret



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {};
        tmap = {};
        for let in s:
            if let in smap:
                smap[let] += 1
            else:
                smap[let] = 1
        for let in t:
            if let in tmap:
                tmap[let] += 1
            else:
                tmap[let] = 1
        return smap == tmap


            
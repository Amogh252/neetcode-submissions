class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        seen = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in seen:
                ret.append(seen[ans])
                ret.append(i)
                return ret
            seen[nums[i]] = i
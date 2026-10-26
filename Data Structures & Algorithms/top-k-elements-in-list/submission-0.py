class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []
        buckets = [[] for i in range(len(nums) + 1)]
        freq_map = {}
        for n in nums:
            if n not in freq_map:
                freq_map[n] = 1
            else:
                freq_map[n] += 1
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        count = 0
        for item in reversed(buckets):
            for num in item:
                ret.append(num)
                count += 1
                if count == k:
                    return ret

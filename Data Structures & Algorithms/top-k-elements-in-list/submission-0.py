class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        sorted_pairs = sorted([(freq, num) for num, freq in counts.items()], reverse=True)
        return [num for freq, num in sorted_pairs[:k]]
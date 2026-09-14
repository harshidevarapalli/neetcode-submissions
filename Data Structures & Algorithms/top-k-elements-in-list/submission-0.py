import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [item[0] for item in heapq.nlargest(k,count.items(),key=lambda x: x[1])]        
from collections import Counter
import heapq

class Solution:
  def topKFrequent(self, words: List[str], k: int) -> List[str]:

    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in frequency.items():
        buckets[freq].append(num)

    
    result = []

    for i in range(len(buckets) - 1, 0, -1):
        if buckets[i]:
            result.extend(buckets[i])
        
            if len(result) >= k:
                return result[:k]

    return result
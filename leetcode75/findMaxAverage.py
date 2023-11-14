class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        s = sum(nums[:k])
        answer = s
        for i in range(k, n):
            s += nums[i]
            s -= nums[i-k]
            answer = max(answer, s)
        return answer/k

# So here in this code we are using a sliding window. We are adding the first k elements and storing it in s.
# Then we are iterating through the rest of the array and adding the next element and removing the first element
# from the sum. Then we are comparing the sum to the answer and storing the max value. Then we are returning the
# answer divided by k. I think this is a good solution. I think I need to practice more with sliding windows.
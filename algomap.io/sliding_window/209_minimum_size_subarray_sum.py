class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sum_target = 0
        min_seq_length = len(nums) + 1

        for r, n in enumerate(nums):
            sum_target += n
            while sum_target >= target and l <= r:
                min_seq_length = min(min_seq_length, r-l+1)
                sum_target -= nums[l]
                l += 1
        
        return min_seq_length if min_seq_length <= len(nums) else 0


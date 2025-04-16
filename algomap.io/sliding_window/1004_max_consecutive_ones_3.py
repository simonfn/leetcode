class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        TOKEN = 1
        start, end = 0, 0
        k_cnt = 0
        longest = 0

        for end in range(len(nums)):
            if nums[end] != TOKEN:
                k_cnt += 1
                while k_cnt > k:
                    if nums[start] != TOKEN:
                        k_cnt -= 1
                    start += 1
            seq_length = end - start + 1
            longest = max(longest, seq_length)

        return longest
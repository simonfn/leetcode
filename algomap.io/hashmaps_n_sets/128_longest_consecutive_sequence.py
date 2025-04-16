class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq = 0

        for num in nums:
            if num-1 not in nums_set:
                seq = 1
                while num+seq in nums_set:
                    seq += 1
                longest_seq = max(longest_seq, seq)
        
        return longest_seq

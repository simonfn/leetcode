class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r and numbers[l] + numbers[r] != target:
            add = numbers[l] + numbers[r]
            if add < target:
                # make it bigger
                l += 1
            else:
                # make it smaller
                r -= 1

        return [l+1, r+1]
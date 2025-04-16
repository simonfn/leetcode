class Solution:
    def maxArea(self, height: List[int]) -> int:
        most = 0
        l, r = 0, len(height)-1
        while l != r:
            volume = (r-l) * min(height[l], height[r])
            most = max(most, volume)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return most


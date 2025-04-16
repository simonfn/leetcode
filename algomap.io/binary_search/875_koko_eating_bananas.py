class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check_k(k, h):
            sum_time = 0
            for n_bananas in piles:
                sum_time += ceil(n_bananas / k)
            
            return sum_time <= h

        l, r = 1, max(piles)
        # find k value in log time
        while l < r:
            m = (l + r) // 2

            if check_k(m, h):
                r = m
            else:
                l = m + 1
        
        return l

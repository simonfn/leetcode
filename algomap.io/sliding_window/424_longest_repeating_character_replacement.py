class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def get_width(l, r):
            return r - l + 1

        seen = dict.fromkeys({ k for k in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' }, 0)
        l = 0
        longest = 0

        for r, c in enumerate(s):
            seen[c] += 1
            while get_width(l, r) - max(seen.values()) > k and l < r:
                c_prev = s[l]
                seen[c_prev] -= 1
                l += 1
            longest = max(longest, get_width(l, r))

        return longest
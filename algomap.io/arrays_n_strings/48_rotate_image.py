class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        LENGTH_MAX = N//2 if N%2==0 else N//2 + 1

        for y in range(LENGTH_MAX):
            for x in range(N//2):
                tl, tr, br, bl = (y, x), (x, N-1-y), (N-1-y, N-1-x), (N-1-x, y)
                tl_saved = matrix[ tl[0] ][ tl[1] ]
                matrix[ tl[0] ][ tl[1] ] = matrix[ bl[0] ][ bl[1] ]
                matrix[ bl[0] ][ bl[1] ] = matrix[ br[0] ][ br[1] ]
                matrix[ br[0] ][ br[1] ] = matrix[ tr[0] ][ tr[1] ]
                matrix[ tr[0] ][ tr[1] ] = tl_saved
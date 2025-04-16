class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        IDENTITY_ELEMENT = 1
        N_LENGTH = len(nums)
        output = [IDENTITY_ELEMENT] * N_LENGTH
        
        # prefixes
        prefixe = IDENTITY_ELEMENT
        for i in range(1, N_LENGTH):
            prefixe *= nums[i-1]
            output[i] = prefixe

        # suffixes
        suffixe = IDENTITY_ELEMENT
        for i in range(N_LENGTH-2, -1, -1):
            suffixe *= nums[i+1]
            output[i] *= suffixe

        return output
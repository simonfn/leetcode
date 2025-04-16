class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        N_TEMPLATE = len(s1)
        template_counter = Counter(s1)
        str_counter = Counter(s2[:N_TEMPLATE])
        
        if template_counter == str_counter:
            return True

        for l, c_r in enumerate(s2[N_TEMPLATE:]):
            r, c_l = l + N_TEMPLATE, s2[l]
            str_counter[c_r] += 1
            str_counter[c_l] -= 1

            if template_counter == str_counter:
                return True

        return False
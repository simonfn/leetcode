class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        N = len(temperatures)
        cold_stack = [] # coldest temperature on top
        answer = [0] * N

        for i, t in enumerate(temps):
            while cold_stack and t > cold_stack[-1][0]:
                old_t, old_i = cold_stack.pop()
                answer[old_i] = i - old_i

            cold_stack.append((t, i))
                
        return answer


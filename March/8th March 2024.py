class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency_map = Counter(nums)
        elements_with_frequency = [(element, frequency_map[element]) for element in set(nums)]
        sorted_elements_with_frequency = sorted(elements_with_frequency, key=lambda x: x[1], reverse=True)

        freq = [i[1] for i in sorted_elements_with_frequency]
        
        highest = max(freq)
        
        ans = 0
        while highest == max(freq):
            ans += max(freq)
            freq.remove(highest)
            
            if freq == []:
                break
            
            
        return ans
    
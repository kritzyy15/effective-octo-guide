class Solution:
    def countFrequencies(self, nums):
        num_frequencies = dict()
        for num in nums:
            num_frequencies[num] = num_frequencies[num] + 1 if num in num_frequencies else 1
            print(num_frequencies[num])
        result = [[k, v] for k, v in num_frequencies.items()]
        return result

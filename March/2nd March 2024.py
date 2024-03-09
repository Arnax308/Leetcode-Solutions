class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        sq = [i ** 2 for i in nums]

        return sorted(sq)
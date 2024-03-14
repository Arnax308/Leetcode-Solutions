class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        ans = 0
        r = 0
        iters = -1

        while True:
            iters += 1
            l = 0
            r = l + iters
            
            if r >= len(nums):
                break

            while r < len(nums):

                if sum(nums[l:r+1]) == goal:
                    ans += 1

                l += 1
                r += 1

        return ans

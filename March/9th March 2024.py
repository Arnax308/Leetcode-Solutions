class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        s1 = set(nums1)
        s2 = set(nums2)

        a = s1.intersection(s2)

        return -1 if len(a) == 0 else min(a)
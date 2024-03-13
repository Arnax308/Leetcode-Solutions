class Solution:
    def pivotInteger(self, n: int) -> int:
        x = math.sqrt(n*(n+1)/2)
        converted = int(x)
        return converted if converted == x else -1

class Solution:
    def customSortString(self, order: str, s: str) -> str:

        ans = []
        sc = Counter(s)

        for i in order:

            if i in s:
                ans.append(i*sc[i])
                sc.pop(i)

        for i in sc:
            ans.append(i*sc[i])

        return ''.join(ans)

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        def r(a, i):
            if type(a[0]) == type('a'):
                return a[i]
            a2, tl, co = a[0]
            if tl * co > i:
                return r(a2, i % tl)
            else:
                return a[i - tl * co + 1]

        o = []
        x = 0
        k -= 1
        for c in s:
            if c.isalpha():
                o.append(c)
                x += 1
            else:
                o = [(o, x, int(c))]
                x *= int(c)
            if x > k:
                break
        return r(o, k)
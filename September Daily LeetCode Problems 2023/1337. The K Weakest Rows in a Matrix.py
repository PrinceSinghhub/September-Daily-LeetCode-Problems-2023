class Solution:
    def kWeakestRows(self, mat, k):
        ans = []
        for index, row in enumerate(mat):
            Sum = (sum(row), index)
            print(Sum)

            ans.append(Sum)

        print(ans)
        ans.sort()
        arr = [i[1] for i in ans[:k]]
        return arr
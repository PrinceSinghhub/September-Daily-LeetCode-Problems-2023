class DSU:
    def __init__(self, n):
        self.rank = [1] * n
        self.root = [i for i in range(n)]

    def find(self, i):
        if self.root[i] == i:
            return i
        return self.find(self.root[i])

    def union(self, i, j):
        ri = self.find(i)
        rj = self.find(j)
        if ri == rj:
            return False
        rki = self.rank[ri]
        rkj = self.rank[rj]
        if rki > rkj:
            self.rank[rkj] = rki
        elif rki < rkj:
            self.rank[rki] = rkj
        else:
            self.rank[ri] += 1
            self.root[ri] = rj
        return True


class Solution:
    def distance(self, x, y):
        i, j = 0, 1
        return abs(x[i] - y[i]) + abs(x[j] - y[j])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)
        pq = list()
        for i in range(n-1):
            for j in range(i+1, n):
                pq.append((self.distance(points[i], points[j]), i, j))

        heapq.heapify(pq)

        ans = 0
        while n - 1 > 0:
            dis, i, j = heapq.heappop(pq)
            if dsu.union(i, j):
                ans += dis
                n -= 1
        return ans
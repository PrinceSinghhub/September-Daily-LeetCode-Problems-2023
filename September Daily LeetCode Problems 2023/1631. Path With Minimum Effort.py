import heapq


class Solution:
    def minimumEffortPath(self, heights):
        visit = set()
        minHeap = [(0, 0, 0)]
        ROWS = len(heights)
        COLS = len(heights[0])

        res = 0
        while minHeap:
            difference, r, c = heapq.heappop(minHeap)

            if (r, c) in visit:
                continue
            res = max(res, difference)
            if r == ROWS - 1 and c == COLS - 1:
                return res

            visit.add((r, c))

            for row, col in [(r + 1, c), (r - 1, c),
                             (r, c - 1), (r, c + 1)]:
                if row >= 0 and row < ROWS and col >= 0 and col < COLS and (row, col) not in visit:
                    newDifference = abs(heights[r][c] - heights[row][col])
                    heapq.heappush(minHeap, (newDifference, row, col))
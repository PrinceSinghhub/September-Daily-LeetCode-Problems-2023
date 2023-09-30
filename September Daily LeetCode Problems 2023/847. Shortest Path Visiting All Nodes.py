class Solution:
    def shortestPathLength(self, graph):

        N = len(graph)

        # M contains all states
        M = (1 << N)
        dp = [[sys.maxsize] * N for _ in range(M)]

        q = []
        for i in range(N):
            # initial states contains all nodes and related states with only one node visited.
            dp[1 << i][i] = 0
            q.append((i, 1 << i))

        # Do BFS
        while q:
            node, state = q.pop(0)
            steps = dp[state][node]
            for x in graph[node]:
                new_state = state | (1 << x)

                # Since all edges have equal distance, BFS is already optimal, so never overwrite
                if dp[new_state][x] == sys.maxsize:
                    dp[new_state][x] = steps + 1
                    q.append((x, new_state))

        # Return minimal steps in state 0b111111...1111
        return min(dp[-1])
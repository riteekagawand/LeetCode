class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        n = len(cost)

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(n):
            for walls in range(n, 0, -1):
                previous = max(0, walls - time[i] - 1)

                dp[walls] = min(
                    dp[walls],
                    cost[i] + dp[previous]
                )

        return dp[n]
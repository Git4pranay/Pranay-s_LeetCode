class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid) + 1
        n = len(obstacleGrid[0]) + 1

        dp = [[0]*n for i in range(m)]
        dp[0][1] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = 0 if obstacleGrid[i - 1][j - 1] == 1 else dp[i - 1][j] + dp[i][j - 1]                

        return dp[m - 1][n - 1]  
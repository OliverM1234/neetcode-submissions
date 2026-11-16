class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        arr = [[0]*n for _ in range(m)]

        arr[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                
                if (i != m-1):
                    arr[i][j] += arr[i+1][j]

                if (j != n-1):
                    arr[i][j] += arr[i][j+1]

        return arr[0][0]

        
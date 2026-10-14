class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        moves = [[0,-1],[0,1],[1,0],[-1,0]]
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0

        def dfs(i,j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == "0":
                return

            grid[i][j] = "0"

            for di, dj in moves:
                dfs(i + di, j + dj)

        islands = 0
        for i1 in range(ROWS):
            for j1 in range(COLS):
                if grid[i1][j1] == "1":
                    islands += 1
                dfs(i1, j1)

        return islands

            
        
        
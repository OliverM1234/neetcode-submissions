class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        HEIGHT = len(board)
        WIDTH = len(board[0])
        visited = set()


        def wordCheck(i,j,curWord, visited):
            if curWord == "":
                return True

            if i < 0 or j < 0 or i >= HEIGHT or j >= WIDTH or curWord[0] != board[i][j] or (i,j) in visited:
                return False

            visited.add((i, j))
            possible = False
            for dx, dy in directions:
                
                possible = possible or wordCheck(i+dx, j+dy, curWord[1:], visited)
                
            visited.remove((i, j))
            return possible


        for i in range(HEIGHT):
            for j in range(WIDTH):
                if (wordCheck(i,j,word,visited)):
                    return True

        return False
        
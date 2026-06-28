class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            
            elems = set()

            for elem in row:
                if elem == ".":
                    continue

                if elem in elems:
                    return False
                
                if int(elem) < 1 or int(elem) > 9:
                    return False

                elems.add(elem)

        for i in range(len(board)):
            
            elems = set()

            for j in range(len(board)):
                elem = board[j][i]

                if elem == ".":
                    continue

                if elem in elems:
                    return False
                
                if int(elem) < 1 or int(elem) > 9:
                    return False

                elems.add(elem)

        for b_i in range(0,2):
            for b_j in range(0,2):
                elems = set()

                for i in range(3):
                    for j in range(3):
                        
                        elem = board[b_i*3+i][b_j*3+j]

                        print(elem, elems)

                        if elem == ".":
                            continue

                        if elem in elems:
                            return False
                        
                        if int(elem) < 1 or int(elem) > 9:
                            return False

                        elems.add(elem)


        return True

            

        
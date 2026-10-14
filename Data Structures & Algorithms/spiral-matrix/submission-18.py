class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        directions = [[1,0],[0,-1],[-1,0],[0,1]]

        out = []

        l, r = 0, len(matrix[0])-1
        TOP, BOTTOM = 0, len(matrix)-1

        while l <= r and TOP <= BOTTOM:

            print(l, r, TOP, BOTTOM, out)

            out += matrix[TOP][l:(r+1)]

            if TOP == BOTTOM:
                break

            print(out)

            for i in range(TOP+1, BOTTOM+1):
                print(i,r, matrix)
                out.append(matrix[i][r])

            
            out += reversed(matrix[BOTTOM][l:r])

            print(out)

            if l == r:
                break

            for i in range(BOTTOM-1, TOP, -1):
                out.append(matrix[i][l])

            l += 1
            r -= 1
            TOP += 1
            BOTTOM -= 1

        return out

        
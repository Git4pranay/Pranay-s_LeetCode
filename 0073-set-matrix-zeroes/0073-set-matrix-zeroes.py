class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        dicrow = set()
        diccol = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    dicrow.add(i)
                    diccol.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in dicrow or j in diccol: matrix[i][j]=0
            
[[1,2,3,4],
 [5,0,7,8],
 [0,10,11,12],
 [13,14,15,0]]

                    



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom =  0 , len(matrix) - 1 
        right , left = len(matrix[0]) - 1 , 0
        l = []
        while top <= bottom and right >= left : 
            for j in range(left ,right+1 ):
                l.append(matrix[top][j])
            top +=1 
            
            for i in range(top ,bottom + 1 ) :
                l.append(matrix[i][right]) 
            right -= 1

            if bottom >= top :

                for k in range(right , left - 1  , -1  ) :
                    l.append(matrix[bottom][k]) 
                bottom -= 1
            if right >= left : 

                for _ in range(bottom , top - 1 , -1  ):
                    l.append(matrix[_][left])
                left += 1
          
        return l

        
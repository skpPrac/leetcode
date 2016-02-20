# https://leetcode.com/problems/spiral-matrix-ii/

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        
        matrix = self.createZeroMatrix(n)
        count = 1
        layers = n/2
        
        if n%2:
            layers += 1
            
        for layer in range(0, layers):
            for j in range(layer, n-layer):
                matrix[layer][j] = count
                count += 1
            
            for i in range(layer+1, n-layer):
                matrix[i][n-1-layer] = count
                count += 1
                
            for j in range(n-2-layer, layer-1, -1):
                matrix[n-layer-1][j] = count
                count += 1
                
            for i in range(n-layer-2, layer, -1):
                matrix[i][layer] = count
                count += 1
                
        return matrix
    
    def createZeroMatrix(self, n):
        matrix = []
        for i in range(0, n):
            row = []
            for j in range(0, n):
                row.append(0)
            matrix.append(row)
        return matrix

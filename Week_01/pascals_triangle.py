class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        triangle = [[1]]
        for i in range(1, numRows):
            triangle.append([
                (0 if j == 0 else triangle[i-1][j-1]) +
                (0 if j == len(triangle[i-1]) else triangle[i-1][j])
                for j in range(i+1)])
        return triangle
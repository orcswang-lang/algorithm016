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

    def generate2(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for _ in range(1, numRows):
            triangle.append(list(map(add, [0] + triangle[-1], triangle[-1] + [0])))
        return triangle if numRows else []

    def generate3(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(numRows):
            # 构建每行的列表,同时设置列首和列尾为1
            row = [1 if i == 0 or i == row_num else None for i in range(row_num + 1)]

            # 每个三角形元素等于这些元素的和
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            triangle.append(row)
        return triangle
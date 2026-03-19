class Solution:
    def generate(self, numRows: int):
        res = [1]
        rows = [[1]]
        for i in range(numRows - 1):
            next_row = [0] * (len(res) + 1)
            for j in range(len(res)):
                next_row[j] += res[j]
                next_row[j+1] += res[j]

            rows.append(next_row)
            res = next_row
            
        return rows
            
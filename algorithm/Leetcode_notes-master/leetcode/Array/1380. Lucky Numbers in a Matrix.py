class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_count = len(matrix)
        column_count = len(matrix[0])

        result = []
        for row in matrix:
            # Identify min value in row and get it's column index
            min_value = min(row)
            min_index = row.index(min_value)
            column_index = 0
            column_max = 0
            # Using the column check for max of that column
            while column_index < row_count:
                if matrix[column_index][min_index] > column_max:
                    column_max = matrix[column_index][min_index]
                column_index += 1
            # If row min equals column max then add it to our results list
            if column_max == min_value:
                result.append(min_value)

        return result
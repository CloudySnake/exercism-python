class Matrix:
    def __init__(self, matrix_string):
        split_string = matrix_string.split("\n")
        self.rows = [list(map(int, row.split(" "))) for row in split_string]
        num_cols = len(self.rows[0])
        self.columns = [[row[col] for row in self.rows] for col in range(num_cols)]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]

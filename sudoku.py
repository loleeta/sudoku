import sys

class CSP:
    def __init__(self, grid):
        self.columns = '123456789'
        self.rows = 'ABCDEFGHI'
        self.board = self.createBoxes() #represents all boxes in the grid
        self.domain = self.createDomain(grid) #current values in the grid
        self.grid = [] #list of columns, rows, subgrids in the grid
        self.setColumns()
        self.setRows()
        self.setSubGrids()

    #generate a set of all boxes in the Sudoku puzzle: A1, A2, A3, etc.
    def createBoxes(self):
        return [r + c for r in self.rows for c in self.columns]

    def printGrid(self):
        print(self.board)

    #creates a list of what is currently on the board based on passed in grid
    def createDomain(self, grid):
        i = 0
        board = {}
        for b in self.board:
            if grid[i] != '0': #if there is already a number in grid
                board[b] = grid[i]
            else:
                board[b] = self.columns #or maybe do 0?
            i = i+1
        return board

    def setCombinations(self):
        combos = []

    #create a list of columns in the grid: A-1+1, A-I+2, A-I+3...
    def setColumns(self):
        columns = [[row + col for row in self.rows for col in column]
                for column in self.columns]
        print(columns)
        self.grid.append(columns)

    #create a list of rows in the grid: A1-9, B1-9, C1-9, D1-9...
    def setRows(self):
        rows = [[row + col for row in rows for col in self.columns]
                for rows in self.rows]
        print(rows)
        self.grid.append(rows)

    #create a list of subgrids in the grid
    def setSubGrids(self):
        subGrids = [[row + col for row in rows for col in cols]
                    for rows in ('ABC', 'DEF', 'GHI') for cols in ('123', '456', '789')]
        self.grid.append(subGrids)



if __name__ == '__main__':
    grid = '060000004' \
              '001403680' \
              '000090000' \
              '002600003' \
              '000007810' \
              '340900070' \
              '003700000' \
              '007000040' \
              '054000001'
    CSP(grid)
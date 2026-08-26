class Spreadsheet:

    def __init__(self, rows: int):
        self.map = {}
        self.limit = rows
     
    def proc(self, cell: str) -> int:
        if len(cell) == 1:
            return int(cell)
        if ord(cell[0]) < 91 and ord(cell[0]) > 64:
            if cell in self.map:
                return self.map[cell]
            return 0
        return int(cell)

    def setCell(self, cell: str, value: int) -> None:
        self.map[cell] = value

    def resetCell(self, cell: str) -> None:
        self.map[cell] = 0

    def getValue(self, formula: str) -> int:
        split = formula.split("+")
        return self.proc(split[0][1::]) + self.proc(split[1])

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
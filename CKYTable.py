from numpy import zeros


class CKYTable:
    table = None

    def __init__(self, tokens):
        self.table = zeros(shape=(len(tokens) + 1, len(tokens) + 1), dtype=CKYCell)
        for i in range(0, len(self.table)):
            for j in range(0, len(self.table)):
                self.table[i, j] = CKYCell()

    def __len__(self):
        return len(self.table)

    def put(self, i, j, item):
        if item not in self.table:
            self.table[i, j] = item

    def get(self, i, j):
        return self.table[i, j]

    def printTable(self):
        for i in range(len(self.table)):
            cells = self.table[i]
            for cell in cells:
                cell.printCell()
            print("")


class CKYCell:
    nonTerminals = []

    def __init__(self):
        self.nonTerminals = []

    def put(self, item):
        self.nonTerminals.append(item)

    def printCell(self):
        for nont in self.nonTerminals:
            print(nont.print_all())

    def setNonTerminals(self, items):
        for item in items:
            self.put(item)
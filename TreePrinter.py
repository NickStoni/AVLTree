"""AVLPrinter is a class which implements printing
the internal structure of the tree into the console,
with print being the main function."""
class AVLPrinter:
    def __init__(self, tree):
        self.tree = tree

    #print - The main function of the AVLPrinter class, which performs the print operation
    #Time complexity O(n)
    def print(self):
        height = self.tree.root.height
        columns = self.calculate_col(height)
        mid = columns//2

        to_print = [[" " for _ in range(columns)] for __ in range(height + 1)]
        self.execute_print(self.tree.root, height, mid, 0, to_print)

        for row in to_print:
            for item in row:
                print(item, end=" ")
            print("")

    #execute_print - A recursive helper function, which fills in "to_print" list
    #Time complexity O(n)
    def execute_print(self, node, height, col, row, to_print):
        if node is None:
            return

        to_print[row][col] = node.data

        shift = 2**(height - 2)

        self.execute_print(node.left, height - 1, col - shift, row + 1, to_print)
        self.execute_print(node.right, height - 1, col + shift, row + 1, to_print)

    #calcualte_col - A helper function used to calculate the size of "to_print" list
    #Time complexity O(n)
    def calculate_col(self, n):
        if n == 0:
            return 1

        return 2 * self.calculate_col(n - 1) + 1
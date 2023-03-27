import TreePrinter as printer
import TreeVisualiser as visualiser

"AVLNode is a helper class which implements nodes in the AVL tree"
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 0

"""AVLTree class implements the AVL tree data structure and all of its functionality.
The class implements, namely, the insert, delete, get max element, get min element, traversal and search operations.
After insert and delete a check is kept on the overall height of the tree. 
The height balance part is taken care by calculating the balance factor of every node. 
The balance factor of a node is the difference between the heights of the left and right subtrees of that node. 
For the tree to be balanced, the balance factor of each node must be within the range {-1, 0, 1}. 
If the balance factor of a node is out of the range, the balance of the tree is restored by 
performing a number of rotations."""
class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.printer = printer.AVLPrinter(self)
        self.visualiser = visualiser.TreeVisualiser(self)

    #insert - Implements insert operation
    #Time complexity O(logn)
    def insert(self, to_insert, node):
        if node is None:
            return to_insert

        if to_insert.data < node.data:
            node.left = self.insert(to_insert, node.left)
        else:
            node.right = self.insert(to_insert, node.right)

        node.height = self.calculate_height(node)
        return self.rebalance(node)

    #delete - Implements delete operation
    #Time complexity O(logn)
    def delete(self, to_delete, node):
        if node is None:
            return None

        if to_delete == node.data:
            if node.left is None:
                #One child or no children
                self.size -= 1
                return node.right

            elif node.right is None:
                self.size -= 1
                return node.left

            else:
                #Two children
                node.data = self.get_max(node.left)
                node.left = self.delete(node.data, node.left)

        elif to_delete > node.data:
            node.right = self.delete(to_delete, node.right)
        else:
            node.left = self.delete(to_delete, node.left)

        node.height = self.calculate_height(node)
        return self.rebalance(node)

    #rebalance - Implements rebalancing the tree
    #Time complexity O(logn)
    def rebalance(self, node):
        balance = self.get_balance(node)

        if balance > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)

            return self.rotate_right(node)
        elif balance < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)

            return self.rotate_left(node)

        return node

    #rotate_left - Implements left rotation of the sub-tree
    #Time complexity O(1)
    def rotate_left(self, node):
        right = node.right
        left_of_right = right.left

        node.right = left_of_right
        right.left = node

        node.height = self.calculate_height(node)
        right.height = self.calculate_height(right)

        return right

    #rotate_right - Implements right rotation of the sub-tree
    #Time complexity O(1)
    def rotate_right(self, node):
        left = node.left
        right_of_left = left.right

        node.left = right_of_left
        left.right = node

        node.height = self.calculate_height(node)
        left.height = self.calculate_height(left)

        return left

    #get_in_order - Implements in-order-traversal of the tree
    #Time complexity O(n)
    def get_in_order(self, node, items):
        if node is None:
            return

        self.get_in_order(node.left, items)
        items.append(node.data)
        self.get_in_order(node.right, items)

    #is_present - Implements the search operation
    #Time complexity O(logn)
    def is_present(self, node, data):
        if node is None:
            return False

        if data == node.data:
            return True
        elif data > node.data:
            return self.is_present(node.right, data)
        else:
            return self.is_present(node.left, data)

    #get_max - Implements retrieving max element from the tree
    #Time complexity O(logn)
    def get_max(self, node):
        if self.is_empty():
            return None

        while node.right is not None:
            node = node.right

        return node.data

    #get_min - Implements retrieving min element from the tree
    #Time complexity O(logn)
    def get_min(self, node):
        if self.is_empty():
            return None

        while node.left is not None:
            node = node.left

        return node.data

    #get_height - Helper function when calculating height of a node
    #Time complexity O(1)
    def get_height(self, node):
        return 0 if node is None else self.calculate_height(node)

    #get_balance - Helper function when calculating balance of a node
    #Time complexity O(1)
    def get_balance(self, node):
        return 0 if node is None else self.get_height(node.left) - self.get_height(node.right)

    #is_empty - Helper function to check if the tree is empty
    #Time complexity O(1)
    def is_empty(self):
        return self.root is None

    #calcualte_height - Helper function to retrieve the height of a node
    #Time complexity O(1)
    def calculate_height(self, node):
        return max(self.get_height(node.left), self.get_height(node.right)) + 1
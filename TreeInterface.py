import AVLTree

"""
Package AVLTree provides a self-balancing tree data structure, 
The package supports a number of operations,
including finding, adding, and removing elements, as well as
returning a graphical representation of the structure.

An AVL tree, a self-balancing binary search tree, is a time-efficient
data structure that can efficiently retrieve elements.

Binary tree is data structure in which each node has at most two children, 
which are referred to as the left child and the right child.

Compared to a common array, an AVL tree performs the operation of
retrieving elements in O(logn) time while using the same amount of memory.

Its benefit compared to a common binary search tree is that the running time complexity remains O(logn),
due to AVL trees being strictly balanced, i.e., the left subtree's height and 
the height of the right subtree differ by at most 1.
While in case of a common binary search tree, worst-case scenario time complexity becomes O(n),
in case the tree gets skewed.

AVL trees are best used for lookup-heavy purposes.
"""

"AVLInterface is used to interact with AVLTree class which implements the data structure"
class AVLInterface:

    def __init__(self):
        self.tree = AVLTree.AVLTree()

    #insert - Inserts the given value as a node into the tree
    #Time complexity O(logn)
    def insert(self, data):
        if data is None:
            return

        self.tree.size += 1
        node = AVLTree.AVLNode(data)

        if self.tree.is_empty():
            root = node
            root.height = self.tree.calculate_height(root)
        else:
            root = self.tree.insert(node, self.tree.root)

        self.tree.root = root
        return self.tree.root

    #delete - Deletes the given value from the tree if the value is present in the tree
    #If multiple nodes are present, removes one occurence
    #Time complexity O(logn)
    def delete(self, data):
        self.tree.root = self.tree.delete(data, self.tree.root)
        return self.tree.root

    #clear - Clears the content of the tree
    #Time complexity O(1)
    def clear(self):
        self.tree.root = None
        self.tree.size = 0

    #is_present - Returns true if the value is present in the tree, otherwise false
    #Time complexity O(logn)
    def is_present(self, data):
        return self.tree.is_present(self.tree.root, data)

    #traverse- Returns a list containing all elements present in the tree
    #Function uses the method called inorder-traversal
    #Time complexity O(n)
    def traverse(self):
        items = []
        self.tree.get_in_order(self.tree.root, items)
        return items

    #get_max - Returns the largest element in the tree
    #Time complexity O(logn)
    def get_max(self):
        return self.tree.get_max(self.tree.root)

    #get_min - Returns the smallest element in the tree
    #Time complexity O(logn)
    def get_min(self):
        return self.tree.get_min(self.tree.root)

    #get_size - Returns the size of the tree
    #Time complexity O(1)
    def get_size(self):
        return self.tree.size

    #is_empty - Returns true if the tree is empty, otherwise false
    #Time complexity O(1)
    def is_empty(self):
        return self.tree.is_empty()

    #print_tree - Prints the structure of the tree
    #Time complexity O(n)
    def print_tree(self):
        if self.tree.is_empty():
            return

        self.tree.printer.print()

    #visualise_tree - Saves an image representing the structure of the tree
    #Time complexity is unknown due to usage of external packages (PIL)
    def visualise_tree(self):
        if self.tree.is_empty():
            return

        self.tree.visualiser.draw_tree()
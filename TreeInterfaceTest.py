import TreeInterface
import collections

class State:
    def __init__(self, is_empty, size):
        self.is_empty = is_empty
        self.size = size

def test_state(tree, expected, message):
    assert tree.is_empty() == expected.is_empty
    assert tree.get_size() == expected.size
    print(message + " state passed")

def test_tree_elements(tree, elements, message):
    for element in elements:
        assert tree.is_present(element) == True

    all_elements = tree.traverse()
    assert collections.Counter(all_elements) == collections.Counter(elements)
    print(message + " tree elements passed")

def test_min_max_elements(tree, min, max, message):
    assert tree.get_min() == min
    assert tree.get_max() == max
    print(message + " min max passed")

def check_is_balanced_BST(node):
    if node is None:
        return

    right = node.right
    left = node.left
    if right is not None and left is not None:
        assert right.data >= left.data
        assert abs(right.height - left.height) <= 1

    check_is_balanced_BST(right)
    check_is_balanced_BST(left)

def test_AVL_tree(tree_interface, message):
    if not tree_interface.is_empty():
        root = tree_interface.tree.root
        check_is_balanced_BST(root)
    print(message + " AVL tree passed")

if __name__ == "__main__":
    #Test API functions: insert, delete, clear, is_present, traverse, get_max, get_min, get_size, is_empty
    tree = TreeInterface.AVLInterface()

    #Test initial state
    case_message = "Initial state"
    test_state(tree, State(True, 0), case_message)

    #Test when inserted a single element
    case_message = "Inserted single element"
    tree.insert(3)
    test_state(tree, State(False, 1), case_message)
    test_tree_elements(tree, [3], case_message)

    #Test convert tree to empty by removing the only element
    case_message = "Turn to empty"
    tree.delete(3)
    test_state(tree, State(True, 0), case_message)

    #Test add multiple elements
    case_message = "Add multiple elements"
    tree.insert(2)
    tree.insert(3)
    tree.insert(3)
    tree.insert(4)
    test_state(tree, State(False, 4), case_message)
    test_tree_elements(tree, [4,2,3,3], case_message)
    test_min_max_elements(tree, 2, 4, case_message)
    test_AVL_tree(tree, case_message)

    #Test clear tree
    case_message = "Clear tree"
    tree.clear()
    test_state(tree, State(True, 0), case_message)

    #Test more different elements
    case_message = "More different elements"
    tree.insert(-1)
    tree.insert(10)
    tree.insert(5)
    tree.insert(-2)
    tree.insert(17)
    tree.insert(100)
    tree.insert(-1)
    tree.insert(3)
    tree.insert(5)
    tree.delete(-1)
    tree.delete(17)
    test_state(tree, State(False, 7), case_message)
    test_tree_elements(tree, [-1, 10, 5, -2, 100, 3, 5], case_message)
    test_min_max_elements(tree, -2, 100, case_message)
    test_AVL_tree(tree, case_message)
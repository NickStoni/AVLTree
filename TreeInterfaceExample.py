import TreeInterface

#Create an instance of the AVLInterface class
tree = TreeInterface.AVLInterface()

#Insert nodes with their respective values
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)

#Return all the elements in the tree in ascending order
traversal = tree.traverse()

#Remove the element with value 5
tree.delete(5)

#Check if element with value 3 is present in the tree
is_three_present = tree.is_present(3)

#Return the largest element in the tree
max = tree.get_max()

#Return the size of the tree
size = tree.get_size()

#Print the tree
tree.print_tree()

#Save an image representing the internal structure of the tree
tree.visualise_tree()

#Delete all elements from the tree
tree.clear()
# Edvin Petterson
# Jonatan Trefil
# Rasmus Jacobsen

# Lab 2
# 2021.12.XX


# Class for creating and handling a Binary Tree
class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)                     # Sets the value of the first node when creating the Tree


    # Checks if a given value exists in the tree
    # Because of the implementation we must always give root as argument
    def search(node, value):
        if value == node.value:                     # Checks if value is in current node
            print("Value is in Tree!")
            return
        elif value < node.value:                    
            if node.left == None:                   # If element is smaller but a smaller does not exists
                print("Value not in Tree =(")
                return
            else:
                search(node.left, value)
                return
        else:
            if node.right == None:                  # If element is larger but a larger does not exists
                print("Value not in Tree =(")
                return
            else:
                search(node.right, value)
                return



    # Prints the Tree out visually
    def display():
        print("temp")



    # Insert a node with a given value into a tree
    def insert():
        print("temp")

# Class for creating a node and it's value
class Node:
    def __init__(self, value):
        self.value = value

    height = None
    parent = None
    left = None
    right = None

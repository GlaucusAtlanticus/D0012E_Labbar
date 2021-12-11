# Edvin Petterson
# Jonatan Trefil
# Rasmus Jacobsen

# Lab 3
# 2021.12.XX

from Node import Node

# Class for creating and handling a Binary Tree
class BinaryTree:
    def __init__(self, value):
        self.root = Node(value, None)                     # Sets the value of the first node when creating the Tree


    # Checks if a given value exists in the tree
    # Because of the implementation we must always give root as argument
    def search(self, node, value):
        if value == node.value:                     # Checks if value is in current node
            return True
        elif value < node.value:                    
            if node.left == None:                   # If element is smaller but a smaller does not exists
                return False
            else:
                return self.search(node.left, value)
        else:
            if node.right == None:                  # If element is larger but a larger does not exists
                return False
            else:
                return self.search(node.right, value)
                

    # Gives a text output to if the value is in the tree
    # Does not need root as argument
    def isValueInTree(self, value):
        answer = self.search(self.root, value)

        if answer:
            print("Value is in the Tree!")
        else:
            print("Value is not in the Tree =(")

        return


    # Prints the Tree out visually
    def display():
        print("temp")



    # Insert a node with a given value into a tree
    def insert(self, node, value):
        if value == node.value:                     # Checks if value is in current node
            return False
        elif value < node.value:                    
            if node.left == None:                   # If element is smaller but a smaller does not exists
                node.left = Node(value, node)
                return True
            else:
                return self.search(node.left, value)     
        else:
            if node.right == None:                  # If element is larger but a larger does not exists
                node.right = Node(value, node)
                return True
            else:
                return self.search(node.right, value)

    
    def delete(self, node, value):
        if value == node.value:
            parent = node.parent
            left = node.left
            right = node.right

            if node.right == None:
                if value < parent.value:
                    parent.left = node.left
                else:
                    parent.right = node.left
            else:
                print("temp")

        elif value < node.value:
            self.delete(node.left, value)
        else:
            self.delete(node.right, value)


def Main():
    tree = BinaryTree(10)

    tree.isValueInTree(15)

    tree.insert(tree.root, 15)

    tree.isValueInTree(15)
Main()
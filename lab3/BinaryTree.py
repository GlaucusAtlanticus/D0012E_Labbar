# Edvin Petterson
# Jonatan Trefil
# Rasmus Jacobsen

# Lab 3
# 2021.12.XX

from Node import Node

# Class for creating and handling a Binary Tree
class BinaryTree:
    def __init__(self, value, c = 0.5):
        self.root = Node(value, None)                     # Sets the value of the first node when creating the Tree
        self.constraint = c

    # Checks if a given value exists in the tree
    # Because of the implementation we must always give root as argument
    def search(self, node, value):
        if value == node.value:                     # Checks if value is in current node
            return node
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

        if answer != False:
            print("Value is in the Tree!")
        else:
            print("Value is not in the Tree =(")

        return


    # Prints the Tree out visually
    def display():
        print("temp")

    def checkConstraint(self, node):
        node.updateSize()
        #print(node.parent)
        if node.parent == None:
            return print("I do not have a parent")
        
        temp = self.constraint * (node.parent.size + 1)

        if node.size > temp:
            print("please rearrange")
        else:
            print("balance as all thing souled be")


    # Insert a node with a given value into a tree
    def insert(self, node, value):
        if value == node.value:                     # Checks if value is in current node
            return False
        elif value < node.value:                    
            if node.left == None:                   # If element is smaller but a smaller does not exists
                node.left = Node(value, node)
                
                print("inserted: ", value)
                self.checkConstraint(node)
                return True
            else:
                temp = self.insert(node.left, value)
                self.checkConstraint(node)
                return temp
        else:
            if node.right == None:                  # If element is larger but a larger does not exists
                node.right = Node(value, node)
                print("inserted: ", value)
                self.checkConstraint(node)
                return True
            else:
                temp = self.insert(node.right, value)
                self.checkConstraint(node)
                return temp

    def delete(self, value):
        node = self.search(self.root, value)
        if node == False:
            print("Kunde inte radera värdet det existerar ej")
            return 

        parent = node.parent
        left = node.left
        right = node.right

        if node.right == None:
            if value < parent.value:
                parent.left = node.left
            else:
                parent.right = node.right
        else:
            leaf = self.searchAndCut(node.right)
        
            leaf.right = right
            leaf.left = left

            if leaf.value < parent.value:
                parent.left = leaf
            else:
                parent.right = leaf

    def searchAndCut(self, node):
        if node.left != None:
            leaf = self.searchAndCut(node.left)
            node.updateSize()
            return leaf
        else:
            node.parent.left = None
            return node


def Main():
    tree = BinaryTree(10)

    #tree.isValueInTree(15)

    tree.insert(tree.root, 15)

    #tree.isValueInTree(15)

    tree.insert(tree.root, 16)

    tree.insert(tree.root, 17)

    tree.insert(tree.root, 18)


Main()
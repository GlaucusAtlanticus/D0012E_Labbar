# Edvin Petterson
# Jonatan Trefil
# Rasmus Jacobsen

# Lab 3
# 2021.12.XX


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
                self.search(node.left, value)
                return
        else:
            if node.right == None:                  # If element is larger but a larger does not exists
                return False
            else:
                self.search(node.right, value)
                return

    # Gives a text output to if the value is in the tree
    # Does not need root as argument
    def isValueInTree(self, value):
        answer = self.search(self, self.root, value)

        if answer:
            print("Value is in the Tree!")
        else:
            print("Value is not in the Tree =(")

        return


    # Prints the Tree out visually
    def display():
        print("temp")



    # Insert a node with a given value into a tree
    def insert(self, value):
        answer = self.search(self, self.root, value)

        if answer:
            print("Answer is already in Tree.")
        else:
            print("temp")



# Class for creating a node and it's value
class Node:
    size = None
    parent = None
    left = None
    right = None

    def __init__(self, value, root):
        self.key = value
        self.parent = root
        self.size = 1

    # returns the nodes size
    def getSize(self):
        return self.size

    # updates the size
    def updateSize(self):       # sums the size of the nodes below it
        temp = 1
        if self.left != None:
            temp += self.left.getSize(self.left)

        if self.right != None:
            temp += self.right.getSize(self.right)

        self.size = temp
    
# Edvin Petterson
# Jonatan Trefil
# Rasmus Jacobsen

# Lab 3
# 2021.12.XX


# Class for creating a node and it's value
class Node:
    def __init__(self, value, root):
        self.value = value              # The key/value that the node holds
        self.parent = root              # Refrence to nodes parent
        
        self.left = None                # Holds node that is lower than current node
        self.right = None               # Holds node that is higher than current node
        self.size = 1

    # updates the size
    def updateSize(self):               # sums the size of the nodes below it
        temp = 1                        # "weight" of the node itself
        if self.left != None:           # If node to the left exists take its sum value
            temp += self.left.size

        if self.right != None:          # If node to the right exists take its sum value
            temp += self.right.size

        self.size = temp                # Size of node is now left size + 1 + right size

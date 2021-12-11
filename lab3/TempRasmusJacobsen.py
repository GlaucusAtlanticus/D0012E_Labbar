# Edvin Petterson
# Jonatan Trefil
# Rasmus Jacobsen

# Lab 3
# 2021.12.XX



# a class for the nodes in the tree
class Node():
    size = None     # how many nodes that are in this node and under it
    parent = None   # this nodes root
    left = None     # the node left of this node
    right = None    # the node right of this node

    def __init__(self, value, root):
        self.value = value  # this nodes value
        self.parent = root  # sets the root node
        self.size = 1       # sets size att one
        #self.c = c          # sets the constraint

    
    ###################################### 
    # Returns this nodes diffrent values #
    ######################################
    def getSize(self):
        return self.size
    def getValue(self):
        return self.value
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def getParent(self):
        return self.parent

    # updates the size
    def updateSize(self):       # sums the size of the nodes below it
        temp = 1
        if self.left != None:
            temp += self.left.getSize(self.left)

        if self.right != None:
            temp += self.right.getSize(self.right)

        self.size = temp

    # creates a child 
    def setLeft(self, node):
        self.left = node
    def setRight(self, node):
        self.right = node

# class for the binary tree
class BinTree():

    # initiates the tree by creating a root node
    def __init__(self, value):
        self.root = Node(value, None)                     # Sets the value of the first node when creating the Tree

    # search up a node whit the right value
    def search(self, node, value):
        if node.getKey() == value:
            return True
        if node.getKey() < value:
            if node.getKey() == None:
                return False
            else:
                self.search(node.getRight(), value)
        if node.getKey() > value:
            if node.getKey() == None:
                return False
            else: 
                self.search(node.getLeft(), value)
    
    # inserts a new value to the tree
    def insert(self, value, node):
        tmp = False

        if node.getKey == value:
            return False
        # if value is to the right of the node
        elif node.getKey() < value:
            if node.getRight() != None:
                tmp = self.insert(value, node.getRight())
            else:
                node.setRight(Node(value, node))
                return True
        # if the value is to the left of the node
        elif node.getKey() > value:
            if node.getLeft() != None:
                tmp = self.insert(value, node.getRight)
            else:
                node.setRight(Node(value, node))
                return True
        
        return tmp
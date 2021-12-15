# Edvin Petterson
# Jonatan Trefil
# Rasmus Jacobsen

# Lab 3
# 2021.12.XX


# Class for creating a node and it's value
from typing import List, Literal


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

    # takes a node an adds it as a child
    def updateChild(self, child):
        child.parent = self             # Update child's parent

        if child.value < self.value:    # IF child is smaller
            self.left = child           #   ADD child to the left
        else:                           # ELSE
            self.right = child          #   ADD child to the right



# Class for creating and handling a Binary Tree
class BinaryTree:
    def __init__(self, value, c = 0.5):
        self.root = Node(value, None)                       # Sets the value of the first node when creating the Tree
        self.constraint = c                                 # Value of the constraint. Higher is more mild constraint allowing for a bigger unbalance.


    # given a value finds node 
    #   Node  = success (node found)
    #   False = value do not exist
    def searchNode(self, value, node = None):
        if node == None:                                    # IF: no node is given
            node = self.root                                # picks tree root as node

        if node.value == value:                             # IF: node value equals value
            return node                                     # return node

        if node.value < value:                              # IF TRUE: walk right

            if node.right == None:                              # can not walk right 
                return False                                    # return False
            else:
                return self.searchNode(value, node.right)       # recursive call to the right
        else:                                               # ELSE: walk left

            if node.left == None:                               # can not walk left
                return False                                    # return False
            else:
                return self.searchNode(value, node.left)        # recursive call to the left

    # Try to insert value in tree 
    #   TRUE  = success
    #   FALSE = value already exist
    def insertNode(self, value, node = None) -> bool:
        if node == None:                                    # IF no node given 
            node = self.root                                # pick tree root as node
        
        if node.value == value:                             # IF node value equals value
            return False                                    # return False

        if node.value < value:                              # IF TRUE: walk right
            if node.right == None:                              # can not walk right
                node.right = Node(value, node)                  # create new node whit value
                return True                                     
            else:
                success = self.insertNode(value, node.right)    # recursive call to the right
                self.check(node)                                # check condition
                return success                                  
        else:                                               # ELSE: walk left
            if node.left == None:                               # can not walk left
                node.left = Node(value, node)                   # create new node whit value
                return True                                     
            else:                                           
                success = self.insertNode(value, node.left)     # recursive call to the left 
                self.check(node)                                # check confition
                return success                                  
    
    # TODO comment
    # takes a list and turns it to a new tree 
    #   Node, the new trees root 
    def listToTree(self, lst) -> Node:
        if len(lst) <= 2:                               # BASE CASE: lst is 2 
            newTree = BinaryTree(lst[0])                #   Create new tree
            try:                                        # Se if it are more element to add
                newTree.insertNode(lst[1])              #   Adds value to new tree
            except IndexError:                          # No more value to add
                i = 1
            return newTree.root                         # Returns new trees root
        
        middle = round(len(lst)/ 2)                     # divide the list in to 
        node = Node(lst[middle], None)                        # create node of the middle element

        leftNode = self.listToTree(lst[:middle])        # recursive call whit the left part of the list
        rightNode = self.listToTree(lst[middle+1:])     # recursive call whit the right part of the list

        node.left = leftNode                            # sets the left child
        leftNode.parent = node                          # updates left child's parent

        node.right = rightNode                          # sets the right child
        rightNode.parent = node                         # updates right child's parent

        return node                                     # return new tree root


    # Dose a in order walk on given node as root
    #   List whit nodes
    def InOrderWalk(self, node = None) -> list:
        if node == None:                                # IF no node given 
            node = self.root                            # pick tree root as node
        
        lst = []                                        # empty list
        if node.left != None:                           # IF: left element
            lst += self.InOrderWalk(node.left)          #   DO: Recursive call on left node
        
        lst += [node.value]                             # ADD node value to list

        if node.right != None:                          # IF: right element 
            lst += self.InOrderWalk(node.right)         #   DO: Recursive call on the right node

        return lst                                      # return list TODO(sorted element pls)

    # Checks if condition tree in balanced 
    def check(self, node) -> bool:
        
        parent = node.parent                            # Saves this nodes parent
        node.updateSize()                               # update this nodes size
        max = self.constraint * (node.size)             # calculate constraint max (break point)

        if (node.left != None) and (max < node.left.size):      # IF left sub tree exist and breaks constraint
            newSubTree = self.rearrange(node)                   #   Rearrange this sub tree
            
            if node == self.root:                               # IF old node was tree root
                self.root = newSubTree                          #   Update tree root
            else:                                               # ELSE
                parent.updateChild(newSubTree)                  #   Update parent child relation
            return True
        elif (node.right != None) and (max < node.right.size):  # If right sub tree exist and breaks constraint
            newSubTree = self.rearrange(node)                   #   Rearrange this sub tree
            
            if node == self.root:                               # IF old node was tree root
                self.root = newSubTree                          #   Update tree root
            else:                                               # ELSE
                parent.updateChild(newSubTree)                  #   Update parent child relation
            return True
        else:
            return False

    # reorders a sub tree
    # returns sub trees root
    def rearrange(self, node) -> Node:
        
        lst = self.InOrderWalk(node)                    # In order walk
        newNode = self.listToTree(lst)                  # Turns a list into a tree
        
        #if node == self.root:                           # IF this node is main tree root
         #   self.root = newNode                         #   Update main tree root

        return newNode

def Main():

    input = 1
    K = 8
    tree = BinaryTree(input)

    while input < K:
        tree.insertNode(input)
        print(input, " inserted")
        input += 1
    print("display:")
    #tree.display()

Main()
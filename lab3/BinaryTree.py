# Edvin Petterson
# Jonatan Trefil
# Rasmus Jacobsen

# Lab 3
# 2021.12.XX

from Node import Node
import math

# Class for creating and handling a Binary Tree
class BinaryTree:
    def __init__(self, value, c = 0.5):
        self.root = Node(value, None)               # Sets the value of the first node when creating the Tree
        self.constraint = c

    # Checks if a given value exists in the tree
    # Because of the implementation we must always give root as argument
    def search(self, node, value):
        if value == node.value:                         # Checks if value is in current node
            return node
        elif value < node.value:                    
            if node.left == None:                       # If element is smaller but a smaller does not exists
                return False                            # Return false as the value therefore does not exist
            else:
                return self.search(node.left, value)    # Checks the next smaller node
        else:
            if node.right == None:                      # If element is larger but a larger does not exists
                return False                            # Return false as the value therefore does not exist
            else:
                return self.search(node.right, value)   # Checks the next larger node
    
    # Gives a text output if the value is in the tree
    # Does not need root as argument
    def isValueInTree(self, value):
        answer = self.search(self.root, value)          # Perform search function

        if answer != False:                             # Value exists
            print("Value is in the Tree!")
        else:                                           # Value does not exist
            print("Value is not in the Tree =(")
        return


    # Prints the Tree out visually
    def display(self):
        queue = [self.root]
        
        while len(queue) != 0:
            if queue[0] != None:
                try:
                    print(queue[0].value, " | ", queue[0].left.value , " ; ", queue[0].right.value)
                except AttributeError:
                    if queue[0].left == None and queue[0].right != None:
                        print(queue[0].value, " | ", queue[0].left , " ; ", queue[0].right.value)
                    elif queue[0].left != None and queue[0].right == None:
                        print(queue[0].value, " | ", queue[0].left.value , " ; ", queue[0].right)
                    else:
                        print(queue[0].value, " | ", queue[0].left , " ; ", queue[0].right)
                 #   print(queue[0], " | ", queue[0] , " ; ", queue[0])
                queue.append(queue[0].left)
                queue.append(queue[0].right)
            queue.pop(0)


    # Updates the sum value of each node and checks if it breaks constraint
    def checkConstraint(self, node):
        node.updateSize()                       # Updates the size
        max = self.constraint * (node.size)     # Calculates constraint * subtree size
        
        if node.left != None:                   # If a subtree to the left exists

            if node.left.size > max:            # Rearrange if left subtree is larger than max allowed value
                print("Rearrange")
            else:
                print("Balance")

        if node.right != None:                  # If a subtree to the right exists

            if node.right.size > max:           # Rearrange if right subtree is larger than max allowed value
                print("Rearrange")
            else:
                print("Balance") 


    # Insert a node with a given value into a tree
    def insert(self, node, value):
        if value == node.value:                         # Checks if value is in current node
            return False                                # Cannot perform insertion as value exists                   
        elif value < node.value:                    
            if node.left == None:                       # If element is smaller but a smaller does not exists
                node.left = Node(value, node)           # Create new node with the value
                
                self.checkConstraint(node)              # Updates size and checks constraint after new node is added
                return True
            else:
                trueFalse = self.insert(node.left, value)   # Checks right node and saves boolean if the operation was sucessfull or not
                self.checkConstraint(node)                  # Updates size and checks constraint as tree might have been modified
                return trueFalse
        else:
            if node.right == None:                      # If element is larger but a larger does not exists
                node.right = Node(value, node)          # Create new node with the value

                self.checkConstraint(node)              # Updates size and checks constraint after new node is added
                return True
            else:
                trueFalse = self.insert(node.right, value)  # Checks right node and saves boolean if the operation was sucessfull or not
                self.checkConstraint(node)                  # Updates size and checks constraint as tree might have been modified
                return trueFalse

    # Made mostly for fun
    # Deletes a node from the tree
    def delete(self, value):
        node = self.search(self.root, value)                # Performs search function to find value
        if node == False:                                   # If value does not exist
            print("Value does not exists in Tree")
            return 

        parent = node.parent                                # Saves the node that is to be deleteds pointers
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

    # This is used ONLY for delete and was made for fun
    # Finds the leftmost node copies it and delets it
    def searchAndCut(self, node):
        if node.left != None:                       # Checks if a node exists to the left
            leaf = self.searchAndCut(node.left)     # Finds the leftmost node, copies it and deletes it
            node.updateSize()                       # Updates the size as now a node is removed
            return leaf
        else:
            node.parent.left = None                 # Delete the connection between the parent and leaf
            return node                             # Return leaf

    # Rotates 2 nodes in tree to the left
    def leftRotation(self, root, pivot):
        root.right = pivot.left             # Switcher the pivots left subtree to the roots right subtree
        pivot.left = root                   # Puts root as the pivots left subtree

        if root == self.root:               # If the root is the actual root of the entire tree we 
            self.root = pivot               # Change so root point to the new root.

        pivot.parent = root.parent          # Makes pivots new parent the parent of root
        root.parent = pivot                 # Makes pivot the parent of root

    # Rotates 2 nodes in tree to the right
    def rightRotation(self, root, pivot):
        root.left = pivot.right             # Switcher the pivots right subtree to the roots left subtree 
        pivot.right = root                  # Puts root as the pivots right subtree

        if root == self.root:               # If the root is the actual root of the entire tree we 
            self.root = pivot               # Change so root point to the new root.

        pivot.parent = root.parent          # Makes pivots new parent the parent of root
        root.parent = pivot                 # Makes pivot the parent of root

def Main():
    tree = BinaryTree(10)

    tree.insert(tree.root, 5)

    tree.insert(tree.root, 15)

    tree.insert(tree.root, 20)

    tree.insert(tree.root, 25)
    tree.display()

Main()
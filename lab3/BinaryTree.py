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
    
    # Gives a text output if the value is in the tree
    # Does not need root as argument
    def isValueInTree(self, value):
        answer = self.search(self.root, value)

        if answer != False:                             
            print("Value is in the Tree!")
        else:
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
        node.updateSize()
        temp = self.constraint * (node.size)
        
        if node.left != None:

            if node.left.size > temp:
                print("please rearrange")
                self.rotate(node.left)
            else:
                print("balance as all thing souled be")

        if node.right != None:

            if node.right.size > temp:
                print("please rearrange")
                self.rotate(node.right)
            else:
                print("Perfectly balanced as all things should be") 


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

    # Deletes a node from the tree
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

    # Finds the leftmost node copies it and delets it
    def searchAndCut(self, node):
        if node.left != None:
            leaf = self.searchAndCut(node.left)
            node.updateSize()
            return leaf
        else:
            node.parent.left = None
            return node

    def rotate(self, node):
        parent = node.parent
        rightOfParent = False
        problemRight = False

        if node.value > parent.value:		#är vi på höger sida av parent
            rightOfParent = True

        if node.left != None and node.right != None:	#vi har 2 barn
            if node.left.size < node.right.size:	# barnen ligger fel
                problemRight = True
        elif node.left == None:				
            problemRight = True
        else:
            problemRight = False
        #####
        
        print("Node size: ", node.value)
        print("How big are you daddy?: ", parent.value)

        print("RightOfParent; ", rightOfParent)
        print("ProblemRight; ", problemRight)
        #######
        if rightOfParent and problemRight:
            print("RightRight")
            
            self.leftRotation(parent, node)


        elif rightOfParent and not problemRight:
            print("RightLeft")
            
            leftChild = node.left
            self.rightRotation(node, node.left)
            parent.right = leftChild
            self.leftRotation(parent, node)
            
        elif (not rightOfParent) and (not problemRight):
            print("LeftLeft")
            
            self.rightRotation(parent, node)
            
        else:
            print("LeftRight")
            
            rightChild = node.right
            self.leftRotation(node, node.right)
            parent.left = rightChild
            self.rightRotation(parent, node)
        print("Mamma")
        self.display()

        
 
    # Rotates 2 nodes in tree to the left
    def leftRotation(self, root, pivot):
        root.right = pivot.left             # Switcher the pivots left subtree
        pivot.left = root


        if root == self.root:               # If the root is the actual root of the entire tree we 
            self.root = pivot               # Change so root point to the new root.

        if root.parent.value > root.value:  #child on rightside
            root.parent.left = pivot
        else :                              #child on lefttside
            root.parent.right = pivot


        pivot.parent = root.parent
        root.parent = pivot

    # Rotates 2 nodes in tree to the right
    def rightRotation(self, root, pivot):
        root.left = pivot.right             
        pivot.right = root

        if root == self.root:               # If the root is the actual root of the entire tree we 
            self.root = pivot               # Change so root point to the new root.

        pivot.parent = root.parent
        root.parent = pivot

def Main():
    tree = BinaryTree(10)

    tree.insert(tree.root, 5)
    tree.display()

    tree.insert(tree.root, 15)
    tree.display()

    tree.insert(tree.root, 20)
    tree.display()

    tree.insert(tree.root, 25)
    tree.display()

Main()
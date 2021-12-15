# Edvin Petterson
# Jonatan Trefil
# Rasmus Jacobsen

# Lab 3
# 2021.12.XX

from Node import Node

# Class for creating and handling a Binary Tree
class BinaryTree:
    def __init__(self, value, c = 0.5):
        self.root = Node(value, None)               # Sets the value of the first node when creating the Tree
        self.constraint = c                         # Value of the constraint. Higher is more mild constraint allowing for a bigger unbalance.

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

            if node.left.size > max:
                print("please rearrange")
                self.rotate(node.left)
            else:
                print("Balance")

        if node.right != None:                  # If a subtree to the right exists

            if node.right.size > max:
                print("please rearrange")
                self.rotate(node.right)
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

        if node.right == None:                              # If a subtree to the right does not exist
            if value < parent.value:                        # And node is smalle than parent
                parent.left = node.left                     # Parents left subtree is now nodes left subtree
            else:
                parent.right = node.left                    # If node is larger than parent we put nodes left subtree as parents right subtree
        else:
            leaf = self.searchAndCut(node.right)            # If a node to the right exists we retrive the leftmost node of it
        
            leaf.right = right                              # Set the deleted node's right subtree as the leafs right subtree
            leaf.left = left                                # Same but left

            if leaf.value < parent.value:                   # Sets the leafs new parent accordingly, if smalle or bigger than parent
                parent.left = leaf
            else:
                parent.right = leaf

    # This is used ONLY for delete and was made for fun
    # Finds the leftmost node copies it and delets it
    def searchAndCut(self, node):
        if node.left != None:                       # Checks if a node exists to the left
            leaf = self.searchAndCut(node.left)     # Finds the leftmost node, copies it and deletes it
            self.checkConstraint(node)              # Updates the size as now a node is removed
            return leaf
        else:
            node.parent.left = None                 # Delete the connection between the parent and leaf
            return node                             # Return leaf

    def rotate(self, node):
        parent = node.parent

        # checks if the right side is larger then the left side
        if node.left == None:
            rightLargerThenLeft = True
        elif node.right == None:
            rightLargerThenLeft = False
        elif node.left.size < node.right.size:
            rightLargerThenLeft = True
        elif node.left.size > node.right.size:
            rightLargerThenLeft = False
        else:
            rightLargerThenLeft = False

        # determens the case
        if parent.value < node.value:
            if rightLargerThenLeft:
                # right right
                self.leftRotation(parent, node)
                print("Right right")
            else:
                # right left
                self.rightRotation(node, node.left)
                self.leftRotation(parent, parent.right)
                print("Right left")
        else:
            if rightLargerThenLeft:
                # left right
                self.leftRotation(node, node.right)
                self.rightRotation(parent, parent.left)
                print("Left right")

            else:
                # left left
                self.rightRotation(parent, node)
                print("Left left")
        self.display()

        
    # Rotates 2 nodes in tree to the left
    def leftRotation(self, parent, pivot):
        leftChild = pivot.left         # In right rot we need to keep track of the left child
        grandParent = parent.parent     # and the grand parent

        parent.right = leftChild        # parent take pivots left child
        
        if leftChild != None:
            leftChild.parent = parent   # pivots left child gets new parent
        
        pivot.left = parent             # pivot takes parent as new left child
        parent.parent = pivot           # parent takes pivot as new parent

        pivot.parent = grandParent      # pivot takes grand parent as parent

        if grandParent == None:         # if grand parent is None that means parent was previous tree root
            self.root = pivot
        else:                           # if it was not update grandparents child
            if grandParent.value < pivot.value:
                grandParent.right = pivot
            else:
                grandParent.left = pivot
        
        parent.updateSize()
        pivot.updateSize()

    # Rotates 2 nodes in tree to the right
    def rightRotation(self, parent, pivot):
        rightChild = pivot.right        # In right rot we need to keep track of the right child
        grandParent = parent.parent     # and the grand parent

        parent.left = rightChild        # parent take pivots right child
        
        if rightChild != None:
            rightChild.parent = parent  # pivots right child gets new parent

        pivot.right = parent            # pivot takes parent as new right child
        parent.parent = pivot           # parent takes pivot as new parent

        pivot.parent = grandParent      # pivot takes grand parent as parent

        if grandParent == None:         # if grand parent is None that means parent was previous tree root
            self.root = pivot
        else:                           # if it was not update grandparents child
            if grandParent.value < pivot.value:
                grandParent.right = pivot
            else:
                grandParent.left = pivot

        parent.updateSize()
        pivot.updateSize()

def Main():
    tree = BinaryTree(10)

    tree.insert(tree.root, 5)
    print("New display")
    tree.display()

    tree.insert(tree.root, 15)
    print("New display")
    tree.display()

    tree.insert(tree.root, 20)
    print("New display")
    tree.display()

    tree.insert(tree.root, 25)
    print("New display")
    tree.display()

Main()
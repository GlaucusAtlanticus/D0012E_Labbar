# Edvin Petterson
# Jonatan Trefil
# Rasmus Jacobsen

# Lab 3
# 2021.12.XX



# to test run the diffrent nodes
from BinaryTree import BinaryTree


def main():
    tree = BinaryTree(10)

    tree.isValueInTree(9)

    tree.insert(tree.root, 9)
    tree.insert(tree.root, 8)
    tree.insert(tree.root, 7)
    
    tree.isValueInTree(7)

    node = tree.searchDelete(tree.root)
    print("Nodens value", node.key)
    tree.isValueInTree(7)

    return "mamma"

main()
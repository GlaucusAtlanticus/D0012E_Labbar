# Edvin Petterson
# Jonatan Trefil
# Rasmus Jacobsen

# Lab 3
# 2021.12.XX


# Class for creating a node and it's value
class Node:
    size = None
    parent = None
    left = None
    right = None

    def __init__(self, value, root):
        self.value = value
        self.parent = root
        self.size = 1
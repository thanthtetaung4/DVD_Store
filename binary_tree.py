from customer import Customer
from BSTNode import BSTNode


class BST:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def insert(self, new_data):
        if self.root is None:
            self.root = BSTNode(new_data)
        else:
            pass

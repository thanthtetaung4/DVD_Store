from customer import Customer
from bstnode import BSTNode


class BST:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
        else:
            if self.root.left is None and data < self.root.data:
                new_node = BSTNode(data)
                self.root.left = new_node
            elif self.root.right is None and data > self.root.data:
                new_node = BSTNode(data)
                self.root.right = new_node

            iterator = self.root
            while iterator is not None:
                current = iterator
                if data < iterator.data:
                    iterator = iterator.left
                elif data > iterator.data:
                    iterator = iterator.right
                else:
                    return False
            new_node = BSTNode(data)
            if data < current.data:
                current.left = new_node
            else:
                current.right = new_node

    def is_leaf(self, node):
        if node.left is None and node.right is None:
            return True





    # def __str__(self):
    #     pass


if __name__ == '__main__':
    bst = BST()
    bst.insert(10)
    bst.insert(15)
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(3)
    bst.insert(2)
    bst.insert(12)
    bst.insert(13)
    bst.insert(11)
    print('-'*10)
    print('BST')
    print(bst.root.data)
    print(bst.root.left.data)
    print(bst.root.right.data)
    print(bst.root.left.data)
    print(bst.root.left.right.data)
    print(bst.root.left.right.right.data)
    print(bst.root.left.left.left.data)
    print(bst.root.right.left.right.data)
    print(bst.root.right.left.left.data)


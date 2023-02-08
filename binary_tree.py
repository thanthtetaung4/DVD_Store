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

            current = self.root
            while current.left is not None or current.right is not None:
                if data < current.data:
                    print(current)
                    current = current.left
                elif data > current.data:
                    print(current)
                    current = current.right
                    print(current)
                else:
                    return False
            print("before", current.data)
            new_node = BSTNode(data)
            if data < current.data:
                current.left = new_node
                print("after", current.left.data)
            else:
                current.right = new_node
                print(new_node.data)
                print("after", current.right.data)






    # def __str__(self):
    #     pass


if __name__ == '__main__':
    bst = BST()
    bst.insert(10)
    bst.insert(20)
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(8)
    bst.insert(9)
    print('-'*10)
    print('BST')
    print(bst.root.data)
    print(bst.root.left.data)
    print(bst.root.right.data)
    print(bst.root.left.left)
    print(bst.root.left.right.data)


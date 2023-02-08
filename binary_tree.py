from customer import Customer
from bstnode import BSTNode
from queue import Queue

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

    def level_order_traverse(self):
        if self.root is None:
            return False

        q = Queue()
        q.enqueue(self.root)
        node = None
        result = []
        while not q.is_empty():
            node = q.dequeue()
            result.append(node)
            if node.get_left() is not None:
                q.enqueue(node.get_left())
            if node.get_right() is not None:
                q.enqueue(node.get_right())
        return result

    def in_order_traverse(self, root, result):
        if not root:
            return
        self.in_order_traverse(root.left, result)
        result.append(root.data)
        self.in_order_traverse(root.right, result)

    def __str__(self):
        output = ''
        node_list = []
        self.in_order_traverse(self.root, node_list)
        for item in node_list:
            output += str(item) + '\t'
        return output


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
    bst.insert(17)
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
    print(bst)


